# bruhcolor

[![Supported Python versions](https://img.shields.io/pypi/pyversions/termcolor.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/bruhcolor/)
[![Downloads](https://static.pepy.tech/badge/bruhcolor)](https://pepy.tech/project/bruhcolor)
[![Downloads](https://static.pepy.tech/badge/bruhcolor/month)](https://pepy.tech/project/bruhcolor)
[![Downloads](https://static.pepy.tech/badge/bruhcolor/week)](https://pepy.tech/project/bruhcolor)
**What is bruhcolor you may ask?**<br/><br/> bruhcolor is a terminal coloring package similar to termcolor with some differences. <br/><br/>First, bruhcolor supports 256 colors (given your terminal can supoprt that). Along with this, it offers a few more options for customizing the text compared to termcolor. <br/><br/>Another major difference is the the use of a wrapper class, rather than returning the escape-sequenced string. When using python's `len()` method on this color-coded strings, it would return a length that included the escape charcaters. Perhaps this is intended in one use case, but for mine it was not. Thus, a wrapper class was made. This wrapper class can give back the length of the pre-colored text when using python's `len()` method. ALong with this, using something like a `f-string` could be trouble some . . . again given the fact the length of a colored string is significantly longer than the orginal text. The wrapper class allows for better formatting with `f-strings`, allowing the formatter to treat the colored text the same as it would the original, unmodified version.

## Installation

### From PyPI

```bash
pip install --upgrade bruhcolor
```

### From source

```bash
git clone https://github.com/ethanlchristensen/bruhcolor
cd bruhcolor
python -m pip install .
```

## Example / Usage

```python
import bruhcolor

# Display all of the color codes
bruhcolor.colors(support="full")

# Simple test message
test_1 = bruhcolor.bruhcolored("Hello World from bruhcolor!", color=24, support="full")
print(test_1)
# Support mult repition
print(test_1 * 5)
print()

# More in depth example
test_2 = bruhcolor.bruhcolored("Hello World from bruhcolor!", color=24, on_color=196, attrs=['blink', 'reverse', 'italic'], support="full")
print(test_2)
print()

test_3 = test_1 + test_2
print(test_3)
test_3 += "How are you doing?"
print(test_3)
print()

# Getting lengths
print(len(test_1))
print(len(test_2))
print(len(test_3))
```
<br/>
<img src="https://i.ibb.co/94RrnQ7/sample-run.png" alt="sample-run" border="0"><br/><br/>
<ul>
  <li>Color Codes: 0 - 255</li>
  <li>Highlight Codes: 0 - 255</li>
  <li>Attributes: blink, reverse, bold, crossed-out, italic, underline, dark, concealed</li>
 </ul>
