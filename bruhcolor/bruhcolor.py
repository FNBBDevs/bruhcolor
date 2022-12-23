# coding: utf-8
# Copyright (c) 2008-2011 Volvox Development Team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Author: Konstantin Lepa <konstantin.lepa@gmail.com>


""" 
256 Color formatting for bruhshell purposes
Format and logic behind some of the code follows
with that of termcolor, the ANSII Color formater
that suported around 8 colors total             
"""

from __future__ import print_function
import os
import re


class bruhcolorwrapper:
    """
    This class serves as a mean to wrap over the 
    color coded text. Wrapping it allows us to 
    get the length of a color coded text ignoring
    the escape sequences. It also allows us to create
    out own format methods so we can properly us the
    f-string in python with a bruhcolored text
    """
    def __init__(self, text, colored):
        self.text = text
        self.colored = colored

    def __len__(self):
        return len(self.text)

    def __str__(self):
        return self.colored

    def __format__(self, fmt):
        if fmt != '':
            if fmt[0] in ['<', '>', '^']:
                spacing = int(fmt[1:])
                if fmt[0] == '<': # left aligned
                    word_size = len(self.text)
                    return self.colored + (' ' * (spacing - word_size))
                elif fmt[0] == '>': # right aligned
                    word_size = len(self.text)
                    return  (' ' * (spacing - word_size)) + self.colored
                elif fmt[0] == '^': # center aligned
                    word_size = len(self.text)
                    left_size = (spacing - word_size) // 2
                    right_size = (spacing - word_size) // 2
                    if (spacing - word_size) % 2 != 0: # If the spacing is odd, add the extra space to the right side
                        right_size += 1
                    return (' ' * left_size)  + self.colored + (' ' * right_size)
                    pass
            else: # default left aligned
                spacing = int(fmt)
                word_size = len(self.text)
                return self.colored + (' ' * (spacing - word_size))
        return self.colored
    
    def __add__(self, addition):
        if isinstance(addition, str):
            tmp = self.copy()
            tmp.text += str(addition)
            tmp.colored += str(addition)
            return tmp
        elif isinstance(addition, bruhcolorwrapper):
            tmp = self.copy()
            tmp.text += addition.text
            tmp.colored += addition.colored
            return tmp
        else:
            print(f"ERROR: when trying to add, [{addition}] must be a string or bruhcolorwrapper")
    
    def __mul__(self, val):
        tmp = self.copy()
        tmp.text *= val
        tmp.colored *= val
        return tmp

    def copy(self):
        text = self.text
        colored = self.colored
        return bruhcolorwrapper(text=text, colored=colored)



__AVAILABLE_COMMANDS__ = ['bruhcolored', 'colors']

VERSION = (0, 0, 1)

# GENERATE THE 256 COLORS -> [38;5;#m for color
COLORS = {}
for i in range(16):
    for j in range(16):
        code = str(i * 16 + j)
        COLORS[code] = u"\u001b[38;5;" + code + "m"
    
# GENERATE THE 256 BACKGROUND COLORS -> [48;5;#m for backgrounf
HIGHLIGHTS = {}
for i in range(16):
    for j in range(16):
        code = str(i * 16 + j)
        HIGHLIGHTS[code] = u"\u001b[48;5;" + code + "m"

# Possible attributes
ATTRIBUTES = {
    'bold': 1,
    'dark': 2,
    'italic': 3,
    'underline': 4,
    'blink': 5,
    'reverse': 7,
    'concealed': 8,
    'crossed-out': 9,
}

# Reset token to restore orginal formatting
RESET = u'\u001b[0m'


def bruhcolored(text, color=None, on_color=None, attrs=None):
    """
    desc:    Generates the properly escape sequenced string for the 
             user inputeed text
    args: 
             text     -> text to be escape sequenced
             color    -> the color code to color the text
             on_color -> the color to set the background
             attrs    -> list of other attributes to apply to the text
    returns: wrapper-object for the colored string
    """
    text, orig_text = str(text), str(text)

    if not color and not on_color and not attrs:
        return text
    
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        if color is not None:
            if str(color) in COLORS:
                text = (COLORS[str(color)] + text)
        if on_color is not None:
            if str(on_color) in HIGHLIGHTS:
                text = '\u001b[' + HIGHLIGHTS[str(on_color)] + text
        if attrs is not None:
            for attr in attrs:
                if attr in ATTRIBUTES:
                    text = '\033[' + str(ATTRIBUTES[attr]) + "m" + text
    return bruhcolorwrapper(orig_text, text + RESET)
    

def colors():
    """
    desc:    prints out all of the colors supported
    args:    None
    returns: None
    """
    for i in range(0, len(COLORS), 16):
        for j in range(i, i + 16):
            c = bruhcolored((' ' * (4 - len(str(j)))) + (str(j)), color=j, on_color=231)
            print(f"{c}", end="")
        print()
    for i in range(0, len(COLORS), 16):
        for j in range(i, i + 16):
            c = bruhcolored((' ' * (4 - len(str(j)))) + (str(j)), color=j, on_color=232)
            print(f"{c}", end="")
        print()


def color_codes():
    return list(range(256))
