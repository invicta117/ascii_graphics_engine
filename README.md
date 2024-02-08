# ASCII Graphics Engine

This ASCII Graphics Engine is a Python package that provides functionality to render objects in ASCII art format. This package can be useful for visualizing simple shapes and designs directly in the terminal.

## Installation

Build the package using the following command:

```bash
python setup.py sdist bdist_wheel
```

You can install the ASCII Renderer package via pip:

```bash
pip install .
```

## Usage

The package can be run directly in the terminal using the following command:

```bash
ascii_graphics_engine
```

Here are some examples of parameters that can be used:

```bash
ascii_graphics_engine --renderer=fill --solid=pyramid
```

```bash
ascii_graphics_engine --renderer=wire --solid=dodecahedron
```

```bash
ascii_graphics_engine --renderer=fill --solid=cube --timeout=0.01
```

```bash
ascii_graphics_engine --help
```

## Contributing

Contributions to the ASCII Renderer project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
