import numpy as np


class Shape:
    """Represents a geometric shape with vertices and edges.

    Args:
        vertices (numpy.ndarray): An array containing the vertices of the shape.
        edges (list): A list of edges connecting the vertices.
        angle (float): The angle (in radians) for rotating the shape.
        surfaces (list): A list of surfaces that are described by a tuple of vertices

    Attributes:
        vertices (numpy.ndarray): An array containing the vertices of the shape.
        edges (list): A list of edges connecting the vertices.
        angle (float): The angle (in radians) for rotating the shape.

    Methods:
        rotate(): Rotates the shape around its center based on the provided angle.
        get_vertices(): Returns the vertices of the shape.
        get_vertex(vertex: int): Returns the specific vertex of the shape.
        get_edges(): Returns the edges of the shape.

    Note:
        This class provides methods to rotate a geometric shape and access its vertices and edges.
    """

    def __init__(self, vertices, edges, angle, surfaces):
        self.vertices = vertices
        self.edges = edges
        self.angle = angle
        self.surfaces = surfaces

    def rotate(self):
        """Rotate the shape around its center based on the stored angle.

        The shape is rotated using 3D rotation matrices along x, y, and z axes.

        Returns:
            numpy.ndarray: Updated vertices after rotation.
        """
        rx = np.array([
            [1, 0, 0],
            [0, np.cos(self.angle), -np.sin(self.angle)],
            [0, np.sin(self.angle), np.cos(self.angle)]
        ])
        ry = np.array([
            [np.cos(self.angle), 0, np.sin(self.angle)],
            [0, 1, 0],
            [-np.sin(self.angle), 0, np.cos(self.angle)]
        ])

        rz = np.array([
            [np.cos(self.angle), -np.sin(self.angle), 0],
            [np.sin(self.angle), np.cos(self.angle), 0],
            [0, 0, 1]
        ])
        self.vertices = np.dot(self.vertices, rx)
        self.vertices = np.dot(self.vertices, ry)
        self.vertices = np.dot(self.vertices, rz)
        return self.vertices

    def get_vertices(self):
        """Get the vertices of the shape.

        Returns:
            numpy.ndarray: Vertices of the shape.
        """
        return self.vertices

    def get_vertex(self, vertex: int):
        """Get a specific vertex of the shape.

        Args:
            vertex (int): Index of the vertex to retrieve.

        Returns:
            numpy.ndarray: Specific vertex of the shape.
        """
        return self.vertices[vertex]

    def get_edges(self):
        """Get the edges of the shape.

        Returns:
            list: Edges connecting the vertices of the shape.
        """
        return self.edges
