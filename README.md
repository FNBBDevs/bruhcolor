# bruhcolor

[![Supported Python versions](https://img.shields.io/pypi/pyversions/termcolor.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/bruhcolor/)
[![Downloads](https://static.pepy.tech/badge/bruhcolor)](https://pepy.tech/project/bruhcolor)
[![Downloads](https://static.pepy.tech/badge/bruhcolor/month)](https://pepy.tech/project/bruhcolor)
[![Downloads](https://static.pepy.tech/badge/bruhcolor/week)](https://pepy.tech/project/bruhcolor)
[![PyPI version](https://badge.fury.io/py/bruhcolor.svg)](https://badge.fury.io/py/bruhcolor)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

bruhcolor is a Python package that allows you to color text in the terminal. It supports 256 colors by using color codes ranging from 0 to 255. Additionally, it provides a set of predefined color names for ease of use.

## Installation

You can install bruhcolor using pip:

```bash
pip install bruhcolor
```

## Usage

Here's an example of how to use bruhcolor:

```python
from bruhcolor import bruhcolored

colored_text = bruhcolored("Hello world!", color="red", on_color=194, attrs=["bold", "blink"])

print(colored_text)
```

This will print "Hello world!" in red color with a background color of 194. The text will also have the attributes of bold and blink.

## Predefined Colors

bruhcolor supports the following predefined colors:

- black
- grey
- red
- green
- yellow
- blue
- magenta
- cyan
- light_grey
- dark_grey
- light_red
- light_green
- light_yellow
- light_blue
- light_magenta
- light_cyan
- white

You can use these color names instead of color codes for convenience.

## Attributes

bruhcolor also supports various text attributes that can be applied to the colored text. These attributes include:

- blink
- reverse
- bold
- crossed-out
- italic
- underline
- dark
- concealed

You can specify multiple attributes by passing them as a list to the `attrs` parameter in the `bruhcolored` function.

## More Examples

Here are a few more examples to demonstrate the usage of bruhcolor:

```python
from bruhcolor import bruhcolored

# Example 1: Colored text with predefined color name
colored_text = bruhcolored("Hello world!", color="green", attrs=["bold"])
print(colored_text)

# Example 2: Colored text with color code
colored_text = bruhcolored("Hello world!", color=123, attrs=["underline"])
print(colored_text)

# Example 3: Colored text with background color
colored_text = bruhcolored("Hello world!", color="blue", on_color="yellow", attrs=["italic"])
print(colored_text)
```

Feel free to explore and experiment with the various color codes, color names, and attributes to customize your terminal text.

## License

bruhcolor is licensed under the MIT License. See [LICENSE](https://github.com/your-username/bruhcolor/blob/main/LICENSE) for more information.
