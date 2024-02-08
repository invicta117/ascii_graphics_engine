import time

from .renderer import Renderer


class WireFrameRenderer(Renderer):
    """Renders wireframe shapes in ASCII art on the screen.

    Inherits from the Renderer class and renders wireframe shapes with specific points and lines.

    Args:
        shape: The shape to be rendered.
        offset (int, optional): The offset value determining the screen size. Defaults to 10.
        timeout (float, optional): The timeout time between shape rotations are rendered. Defaults to 0.05.

    Attributes:
        Inherits attributes from the Renderer class:
            point (str): The character representing a single point in the rendered wireframe.
            line (str): The character representing a line in the rendered wireframe.

    Methods:
        __draw_line(point1, point2): Draws a line between two points on the screen.
        __draw_point(*points): Draws a point on the screen.
        __wire_shape(): Draws the wireframe representation of the provided shape.
        run(): Continuously rotates the shape and renders its wireframe representation on the screen.

    Note:
        This class provides functionality to render wireframe shapes by rotating and displaying them in ASCII art.
    """

    def __init__(self, shape, offset=10, timeout=0.05):
        self.point = "*"
        self.line = "."
        self.timeout = timeout
        super().__init__(shape, offset)

    def __draw_line(self, point1, point2):
        x1, y1, *_ = point1
        x2, y2, *_ = point2
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if x1 < x2:
            sx = 1
        else:
            sx = -1
        if y1 < y2:
            sy = 1
        else:
            sy = -1
        error = dx - dy
        while True:
            if self.pixels[self.offset + x1][self.offset + y1] != self.point:
                self.pixels[self.offset + x1][self.offset + y1] = self.line
            if x1 == x2 and y1 == y2:
                break
            error_2 = 2 * error
            if error_2 > -dy:
                error -= dy
                x1 += sx
            if error_2 < dx:
                error += dx
                y1 += sy

    def __draw_point(self, *points):
        """Draws a point on the screen based on the provided coordinates."""
        x, y, *_ = points
        self.pixels[self.offset + int(x)][self.offset + int(y)] = self.point

    def __wire_shape(self):
        """Draws the wireframe representation of the shape."""
        for x, y, z in self.shape.get_vertices():
            self.__draw_point(x, y)

        for edge in self.shape.get_edges():
            self.__draw_line(self.shape.get_vertex(edge[0]), self.shape.get_vertex(edge[1]))

    def run(self):
        """Continuously rotates the shape and renders its wireframe representation on the screen."""
        while True:
            self.shape.rotate()
            self.__wire_shape()
            self._draw_screen()
            time.sleep(self.timeout)
