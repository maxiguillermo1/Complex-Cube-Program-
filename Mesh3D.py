from OpenGL.GL import *

class Mesh3D:
    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces

    @property
    def edges(self):
        return [(face[i], face[(i + 1) % 3]) for face in self.faces for i in range(3)]

    def draw(self):
        glBegin(GL_TRIANGLES)
        for face in self.faces:
            for vertex in face:
                glVertex3fv(self.vertices[vertex])
        glEnd()

def create_cube_mesh(color):
    verts = [
        [0.5, 0.5, -0.5],
        [-0.5, 0.5, -0.5],
        [-0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5],
        [0.5, 0.5, 0.5],
        [-0.5, 0.5, 0.5],
        [-0.5, -0.5, 0.5],
        [0.5, -0.5, 0.5],
    ]
    tris = [
        (0, 1, 2),
        (0, 2, 3),
        (4, 0, 3),
        (4, 3, 7),
        (5, 4, 7),
        (5, 7, 6),
        (1, 5, 6),
        (1, 6, 2),
        (4, 5, 1),
        (4, 1, 0),
        (2, 6, 7),
        (2, 7, 3),
    ]

    return Mesh3D(verts, tris)