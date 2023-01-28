from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.53'
DESCRIPTION = '256 Color Terminal Text Formatter'
LONG_DESCRIPTION = 'A package that allows for various text modifications to terminal ouput in python.'

# Setting up
setup(
    name="bruhcolor",
    version=VERSION,
    author="Ethan Christensen",
    author_email="ethanlchristensen@outlook.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'terminal', 'text coloring', 'bruhcolor'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)