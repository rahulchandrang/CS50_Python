# Demonstrates IndexError
# sys is mainly command line arguments

import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

# To run > python name1.py Rahul