# Demonstrates sys.argv

import sys

print("hello, my name is", sys.argv[1])

# The location 0 sys.argv[0] takes the file name thats why we give [1] in the program
# If we wnat to give full name we can use > python name3.py "Rahul Chandran"