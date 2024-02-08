import math

import numpy as np
from numpy import pi

from .shape import Shape


class Pyramid(Shape):
    """Represents a pyramid-shaped 3D object.

    Inherits from the Shape class and defines a pyramid with specified size and angle.

    Args:
        size (float): The size of the pyramid.
        angle (float, optional): The angle in radians for the pyramid's orientation. Defaults to pi / 32.

    Attributes:
        Inherits attributes from the Shape class:
            vertices (numpy.ndarray): An array containing the vertices of the pyramid.
            edges (list): A list of edges connecting the vertices.
            angle (float): The angle (in radians) for the pyramid's orientation.
            surfaces (list): A list of surfaces representing the pyramid's faces.

    Note:
        The pyramid is defined by its vertices, edges, angle, and surfaces connecting the vertices.
    """

    def __init__(self, size, angle=pi / 32):
        vertices = np.array([
            [-1.0, -1.0, -1.0],  # Base vertex 1
            [1.0, -1.0, -1.0],  # Base vertex 2
            [1.0, 1.0, -1.0],  # Base vertex 3
            [-1.0, 1.0, -1.0],  # Base vertex 4
            [0, 0, 1.0]  # Apex vertex
        ])
        vertices /= math.sqrt(3)
        vertices *= size
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),  # Base edges
            (0, 4), (1, 4), (2, 4), (3, 4)  # Edges connecting base to apex
        ]
        surfaces = [((0, 1), (1, 2), (2, 3), (3, 0)),
                    ((0, 4), (4, 3), (3, 0)),
                    ((3, 2), (2, 4), (4, 3)),
                    ((2, 1), (1, 4), (4, 2)),
                    ((1, 4), (4, 0), (0, 1))
                    ]
        super().__init__(vertices, edges, angle, surfaces)
