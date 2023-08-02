from OpenGL.GL import *

class Object3D:
    def __init__(self, mesh, screen_width, screen_height):
        self.mesh = mesh
        self.position = [0, 0, 0]
        self.orientation = [0, 0, 0]
        self.scale = [1, 1, 1]
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glRotatef(self.orientation[0], 1, 0, 0)
        glRotatef(self.orientation[1], 0, 1, 0)
        glRotatef(self.orientation[2], 0, 0, 1)
        glScalef(*self.scale)
        self.mesh.draw()
        glPopMatrix()

