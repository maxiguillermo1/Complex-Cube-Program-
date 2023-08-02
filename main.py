import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Mesh3D import create_cube_mesh
from Object3D import Object3D
import math
import random


# Configuration section for perspective, rotations, and transformations
config = {
    'translation_speed': 0.01,
    'rotation_speed': 0.0,
    'movement_speed': 0.01,
    'v_fov': 45,
    'near': 0.1,
    'far': 50,
    'camera_position': [0, 0, 5],
    'camera_target': [0, 0, 0],
    'camera_up': [0, 1, 0],
    'yaw': 0.0,
    'pitch': 0.01,
    'roll': 0.0,
    'camera_speed': 0.05
}

def make_cube(position, color, screen_width, screen_height):
    cube = Object3D(create_cube_mesh(color), screen_width, screen_height)
    cube.position = position
    cube.orientation = [0, 0, 0]
    scale_factor = 2
    cube.scale = [scale_factor, scale_factor, scale_factor]
    return cube

if __name__ == "__main__":
    pygame.init()
    screen_width = 1000
    screen_height = 1000
    pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

    cubes = []
    position = [0, 0, 0]  # Position for the cube to spawn at the center of the scene
    color = (255, 255, 255)  # White color for the cube
    cubes.append(make_cube(position, color, screen_width, screen_height))

    v_fov = config['v_fov']
    near = config['near']
    far = config['far']
    top = math.tan(math.radians(v_fov)) * near
    right = top * screen_width / screen_height
    left = -right
    bottom = -top

    clock = pygame.time.Clock()

    done = False
    frame = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            config['pitch'] += config['camera_speed']
        if keys[K_s]:
            config['pitch'] -= config['camera_speed']
        if keys[K_a]:
            config['yaw'] -= config['camera_speed']
        if keys[K_d]:
            config['yaw'] += config['camera_speed']

        config['camera_position'][0] = 5 * math.sin(config['yaw']) * math.cos(config['pitch'])
        config['camera_position'][1] = 5 * math.sin(config['pitch'])
        config['camera_position'][2] = 5 * math.cos(config['yaw']) * math.cos(config['pitch'])

        if done:
            break

        glViewport(0, 0, screen_width, screen_height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(v_fov, screen_width / screen_height, near, far)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(*config['camera_position'], *config['camera_target'], *config['camera_up'])

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for cube in cubes:
            cube.draw()

        pygame.display.flip()
        clock.tick(60)
        frame += 1
        if frame >= 1000:
            frame = 0

    pygame.quit()
