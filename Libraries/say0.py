# Demonstrates pip-installed package

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

# pypi.org/project/cowsay . cowsay is a package in pypi. We need to use pypi to install it