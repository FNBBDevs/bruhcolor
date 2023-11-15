# bruhcolor

[![Supported Python versions](https://img.shields.io/pypi/pyversions/termcolor.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/bruhcolor/)
[![Downloads](https://static.pepy.tech/badge/bruhcolor)](https://pepy.tech/project/bruhcolor)
[![Downloads](https://static.pepy.tech/badge/bruhcolor/month)](https://pepy.tech/project/bruhcolor)
[![Downloads](https://static.pepy.tech/badge/bruhcolor/week)](https://pepy.tech/project/bruhcolor)
[![PyPI version](https://badge.fury.io/py/bruhcolor.svg)](https://badge.fury.io/py/bruhcolor)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# bruhcolor

bruhcolor is a Python package that allows you to color text in the terminal. It supports both 8-color and 256-color formatting, providing a wide range of colors to choose from. The package is available on PYPI and is licensed under the MIT license.

## Installation

To install bruhcolor, you can use pip:

```shell
pip install bruhcolor
```

## Usage

To use bruhcolor, simply import the `bruhcolored` function from the package:

```python
from bruhcolor import bruhcolored
```

You can then use the `bruhcolored` function to color your text. Here's an example:

```python
colored_text = bruhcolored("Hello world!", color="red", on_color=194, attrs=["bold", "blink"])

print(colored_text)
```

This will output the text "Hello world!" in red color, with a background color of 194 and the attributes "bold" and "blink" applied.

## Available Colors

bruhcolor supports a wide range of colors. You can use either the 8-color or 256-color formatting. Here are some examples of available colors:

- 8-color: black, grey, red, green, yellow, blue, magenta, cyan, light_grey, dark_grey, light_red, light_green, light_yellow, light_blue, light_magenta, light_cyan, white
- 256-color: You can use any number between 0 and 255 to specify a color.

To see a full list of available colors, you can use the `colors` function:

```python
from bruhcolor import colors

colors(support="full")
```

This will print out all the available colors.

## Available Attributes

bruhcolor also supports various attributes that you can apply to your text. Here are some examples of available attributes:

- bold
- dark
- italic
- underline
- blink
- reverse
- concealed
- crossed-out

To see a full list of available attributes, you can use the `valid_effects` function:

```python
from bruhcolor import valid_effects

valid_effects()
```

This will print out all the available attributes.

## Additional Information

For more information on how to use bruhcolor, you can refer to the [bruhcolor documentation](https://github.com/ethanlchristensen/bruhcolor).

## License

bruhcolor is licensed under the MIT License. See [LICENSE](https://github.com/your-username/bruhcolor/blob/main/LICENSE) for more information.
