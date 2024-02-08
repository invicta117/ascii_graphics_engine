import math

import numpy as np
from numpy import pi

from .shape import Shape


class Dodecahedron(Shape):
    """Represents a dodecahedron-shaped 3D object.

        Inherits from the Shape class and defines a dodecahedron with specified size and angle.

        Args:
            size (float): The size of the dodecahedron.
            angle (float, optional): The angle in radians for the dodecahedron's orientation. Defaults to pi / 32.

        Attributes:
            Inherits attributes from the Shape class:
                vertices (numpy.ndarray): An array containing the vertices of the dodecahedron.
                edges (list): A list of edges connecting the vertices.
                angle (float): The angle (in radians) for the dodecahedron's orientation.
                surfaces (list): A list of surfaces representing the dodecahedron's faces.

        Note:
            The dodecahedron is defined by its vertices, edges, angle, and surfaces connecting the vertices.
            The 'size' parameter determines the overall size of the dodecahedron.
        """

    def __init__(self, size, angle=pi / 32):
        phi = (1 + 5 ** 0.5) / 2  # Golden ratio
        vertices = np.array([
            (1, 1, 1),
            (1, 1, -1),
            (1, -1, 1),
            (1, -1, -1),
            (-1, 1, 1),
            (-1, 1, -1),
            (-1, -1, 1),
            (-1, -1, -1),
            (0, 1 / phi, phi),
            (0, -1 / phi, phi),
            (0, 1 / phi, -phi),
            (0, -1 / phi, -phi),
            (1 / phi, phi, 0),
            (-1 / phi, phi, 0),
            (1 / phi, -phi, 0),
            (-1 / phi, -phi, 0),
            (phi, 0, 1 / phi),
            (phi, 0, -1 / phi),
            (-phi, 0, 1 / phi),
            (-phi, 0, -1 / phi)
        ])
        vertices /= math.sqrt(3)
        vertices *= size
        edges = [
            (6, 18), (6, 15), (12, 13), (5, 13), (5, 10), (8, 9), (4, 18), (5, 19), (0, 8), (2, 14), (1, 12), (7, 19),
            (18, 19), (4, 8), (14, 15), (10, 11), (0, 16), (2, 16), (1, 17), (7, 15), (3, 11), (3, 14), (4, 13),
            (3, 17), (0, 12), (2, 9), (1, 10), (7, 11), (6, 9), (16, 17)
        ]
        surfaces = [((0, 12), (1, 17), (12, 1), (16, 0), (17, 16)),
                    ((4, 18), (6, 9), (8, 4), (9, 8), (18, 6)),
                    ((6, 18), (7, 15), (15, 6), (18, 19), (19, 7)),
                    ((2, 9), (6, 15), (9, 6), (14, 2), (15, 14)),
                    ((0, 16), (2, 9), (8, 0), (9, 8), (16, 2)),
                    ((2, 14), (3, 17), (14, 3), (16, 2), (17, 16)),
                    ((3, 11), (7, 15), (11, 7), (14, 3), (15, 14)),
                    ((1, 17), (3, 11), (10, 1), (11, 10), (17, 3)),
                    ((0, 12), (4, 8), (8, 0), (12, 13), (13, 4)),
                    ((1, 12), (5, 10), (10, 1), (12, 13), (13, 5)),
                    ((5, 10), (7, 19), (10, 11), (11, 7), (19, 5)),
                    ((4, 18), (5, 13), (13, 4), (18, 19), (19, 5))]

        super().__init__(vertices, edges, angle, surfaces)
