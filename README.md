# Complex Cube Program using OpenGL and Pygame

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [How to Run](#how-to-run)
5. [Implementation Details](#implementation-details)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

This project aims to create a complex 3D cube simulation using OpenGL for rendering and Pygame for handling user input and the game loop.

## Requirements

- Python 3.x
- PyOpenGL
- Pygame

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/yourrepository.git
    ```

2. Navigate into the project directory:

    ```
    cd yourrepository
    ```

3. Install the required packages:

    ```
    pip install PyOpenGL Pygame
    ```

## How to Run

1. Make sure you are in the project directory.

2. Run the main Python file:

    ```
    python main.py
    ```

## Implementation Details

### Mesh and Object 3D

The core of this program relies on two main classes, `Mesh3D` and `Object3D`. `Mesh3D` is responsible for storing the vertices and faces of the 3D object. The `Object3D` class inherits `Mesh3D` and adds transformations like translation, rotation, and scaling.

### Perspective Configuration

The program uses a perspective projection configured with a vertical field of view (`v_fov`), near and far clipping planes, and the aspect ratio derived from the screen dimensions.

### Camera Controls

Yaw and pitch camera controls are implemented, allowing the user to move the camera using the W, A, S, D keys.

### Main Loop

The main game loop handles event polling, camera updating, and rendering. Each frame, the 3D cube is drawn onto the screen.

### Shader

The vertex shader transforms the vertex positions and normals according to the model, view, and projection matrices.

### Difficulty Level

This program is moderately complex, requiring a good understanding of OpenGL's pipeline, 3D transformations, and Pygame's event loop. The use of shaders adds another layer of complexity, requiring knowledge of GLSL.

## Contributing

If you wish to contribute, please fork the repository and submit a pull request.

## License

MIT License. Please see the `LICENSE` file for more information.
