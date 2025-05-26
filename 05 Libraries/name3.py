# Demonstrates sys.exit

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

# There will be IndexError in this code if we run this python name3.py. if we used if len(sys.argv) < 2:
#    print("Too few arguments")
# elif len(sys.argv) > 2:
#    print("Too many arguments"). Because of this we use sys.exit