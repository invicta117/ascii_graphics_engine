import math

import numpy as np
from numpy import pi

from .shape import Shape


class Cube(Shape):
    """Represents a cube-shaped 3D object.

        Inherits from the Shape class and defines a cube with specified size and angle.

        Args:
            size (float): The size of the cube.
            angle (float, optional): The angle in radians for the cube's orientation. Defaults to pi / 32.

        Attributes:
            Inherits attributes from the Shape class:
                vertices (numpy.ndarray): An array containing the vertices of the cube.
                edges (list): A list of edges connecting the vertices.
                angle (float): The angle (in radians) for the cube's orientation.
                surfaces (list): A list of surfaces representing the cube's faces.

        Note:
            The cube is defined by its vertices, edges, angle, and surfaces connecting the vertices.
            The 'size' parameter determines the overall size of the cube.
        """

    def __init__(self, size, angle=pi / 32):
        vertices = np.array([[-1.0, 1.0, 1.0],
                             [-1.0, 1.0, -1.0],
                             [1.0, 1.0, -1.0],
                             [1.0, 1.0, 1.0],
                             [-1.0, -1.0, 1.0],
                             [-1.0, -1.0, -1.0],
                             [1.0, -1.0, -1.0],
                             [1.0, -1.0, 1.0]])
        vertices /= math.sqrt(3)
        vertices *= size
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
            (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
            (0, 4), (1, 5), (2, 6), (3, 7)  # Connections between top and bottom faces
        ]
        surfaces = [((0, 1), (1, 2), (2, 3), (3, 0)),
                    ((0, 3), (3, 7), (7, 4), (4, 0)),
                    ((0, 1), (1, 5), (5, 4), (4, 0)),
                    ((1, 2), (2, 6), (6, 5), (5, 1)),
                    ((4, 5), (5, 6), (6, 7), (7, 4)),
                    ((3, 2), (2, 6), (6, 7), (7, 3)),
                    ]
        super().__init__(vertices, edges, angle, surfaces)
