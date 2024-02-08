from abc import ABC, abstractmethod


class Renderer(ABC):
    """Abstract base class for rendering shapes on a screen.

    Args:
        shape: The shape to be rendered.
        offset (int): The offset value determining the screen size.

    Attributes:
        offset (int): The offset value determining the screen size.
        shape: The shape to be rendered.
        pixels (list): A 2D list representing the screen pixels.

    Methods:
        __clear(): Clears the screen pixels.
        _draw_screen(): Draws the screen with the rendered shape.
        run(wire_shape: bool): Abstract method to execute the rendering process.
    """

    def __init__(self, shape, offset):
        self.offset = offset
        self.shape = shape
        self.pixels = [[" " for _ in range(self.offset * 2 + 1)] for _ in range(self.offset * 2 + 1)]

    def __clear(self):
        """Clears the screen pixels."""
        self.pixels = [[" " for _ in range(self.offset * 2 + 1)] for _ in range(self.offset * 2 + 1)]

    def _draw_screen(self):
        """Draws the screen with the rendered shape."""
        print()
        for i in range(len(self.pixels) - 1, -1, -1):
            for j in range(len(self.pixels[0])):
                print(self.pixels[i][j], sep="", end="")
            print(end="\n")
        print()
        self.__clear()

    @abstractmethod
    def run(self):
        """Execute the rendering process."""
        pass
