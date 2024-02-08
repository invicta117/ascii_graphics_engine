import argparse

from .renderer.solidfillrenderer import SolidFillRenderer
from .renderer.wireframerenderer import WireFrameRenderer
from .shapes.cube import Cube
from .shapes.dodecahedron import Dodecahedron
from .shapes.pyramid import Pyramid


def main():
    """Entry point for the console script.

    This script is a simple game engine renders a shape using ascii.

    Usage:
        python runner.py [options]

    Options:
        -h, --help          Show this help message and exit
        -r, --renderer      Select mode: (default: wire, fill)
        -s, --solid         Select solid: (default: cube, pyramid, dodecahedron)
        -t, --timeout       Select timeout between frame renders in seconds: (default: 0.05)
        -S, --size          Select screen size in ascii chars: (default: 10)
    """
    parser = argparse.ArgumentParser(
        description='Simple game engine that offers a fun and interactive way to visualize different shapes using '
                    'ASCII characters')
    parser.add_argument('--renderer', '-r', type=str, default='wire', choices=['wire', 'fill'],
                        help='Select mode: (default: wire, fill)')
    parser.add_argument('--solid', '-s', type=str, default='cube', choices=['cube', 'pyramid', 'dodecahedron'],
                        help='Select solid: (default: cube, pyramid, dodecahedron)')
    parser.add_argument('--timeout', '-t', type=float, default=0.05,
                        help='Select timeout: (default: 0.05)')
    parser.add_argument('--size', '-S', type=int, default=10,
                        help='Select screen size in ascii chars: (default: 10)')
    args = parser.parse_args()
    selected_solid = args.solid
    selected_renderer = args.renderer
    selected_size = args.size
    timeout = args.timeout

    if selected_solid == "pyramid":
        solid = Pyramid(selected_size)
    elif selected_solid == "dodecahedron":
        solid = Dodecahedron(selected_size)
    else:
        solid = Cube(selected_size)

    runner = WireFrameRenderer(solid, offset=selected_size, timeout=timeout)
    if selected_renderer == "fill":
        runner = SolidFillRenderer(solid, offset=selected_size, timeout=timeout)

    runner.run()


if __name__ == "__main__":
    main()
