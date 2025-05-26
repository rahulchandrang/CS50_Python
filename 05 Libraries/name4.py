# Demonstrates list slice

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: #Here we are mentioning start and end number. Here start is 1 and we dont have end. Also try with [1:]:
    print("hello, my name is", arg)
