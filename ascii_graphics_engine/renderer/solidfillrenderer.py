import time

from .renderer import Renderer


class SolidFillRenderer(Renderer):
    """Renders solid-filled shapes on the screen.

        Inherits from the Renderer class and renders shapes with solid colors based on their surfaces.

        Args:
            shape: The shape to be rendered.
            offset (int, optional): The offset value determining the screen size. Defaults to 10.
            timeout (float, optional): The timeout time between shape rotations are rendered. Defaults to 0.05.

        Attributes:
            Inherits attributes from the Renderer class:
                face_colour (dict): A dictionary mapping surface indices to their corresponding colors.

        Methods:
            __ray_cast(pixel_y, pixel_x, surface): Performs ray casting to determine if a pixel lies within a surface.
            __surface_distance_from_viewpoint(surface): Calculates the average distance of a surface from the viewpoint.
            __fill_shape(): Fills the shape with colors based on surface intersection.
            run(): Continuously rotates the shape and renders its solid-filled representation on the screen.

        Note:
            This class provides functionality to render solid-filled shapes by casting rays onto surfaces.
        """

    def __init__(self, shape, offset=10, timeout=0.05):
        super().__init__(shape, offset)
        self.face_colour = {surface: f"{chr(37 + k)}" for k, surface in enumerate(self.shape.surfaces)}
        self.timeout = timeout

    def __ray_cast(self, pixel_y, pixel_x, surface):
        """Performs ray casting to determine if a pixel lies within a surface."""
        intersections = 0
        for edge in surface:
            y1, x1, *_ = self.shape.get_vertex(edge[0])
            y2, x2, *_ = self.shape.get_vertex(edge[1])
            if x2 - x1 == 0:
                continue
            m = (y2 - y1) / (x2 - x1)
            c = y1 - (m * x1)
            y = (m * pixel_x) + c
            if pixel_y < y and min(y1, y2) < y < max(y1, y2):
                intersections += 1
        return intersections % 2 != 0

    def __surface_distance_from_viewpoint(self, surface):
        """Calculates the average distance of a surface from the viewpoint."""
        camera_z = self.offset
        average_dist = 0
        for edge in surface:
            _, _, z = self.shape.get_vertex(edge[0])
            average_dist += abs(camera_z - z)
        return average_dist

    def __fill_shape(self):
        """Fills the shape with colors based on surface intersection."""
        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[0])):
                for k, surface in enumerate(
                        sorted(self.shape.surfaces, key=self.__surface_distance_from_viewpoint, reverse=True)):
                    if self.__ray_cast(i - self.offset, j - self.offset, surface):
                        self.pixels[i][j] = self.face_colour[surface]

    def run(self):
        """Continuously rotates the shape and renders its solid-filled representation on the screen."""
        while True:
            self.shape.rotate()
            self.__fill_shape()
            self._draw_screen()
            time.sleep(self.timeout)
