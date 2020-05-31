#! /usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("ERROR")
    sys.exit(1)
try:
    nb = int(sys.argv[1])
except ValueError:
    print("ERROR")
    sys.exit(1)

if nb == 0:
    print("I'm Zero.")
elif nb % 2 is 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
