#! /usr/bin/env python3

import sys
import string


def err():
    print("ERROR")
    sys.exit(1)


def prout():
    len(sys.argv) == 3 or err()
    try:
        size = int(sys.argv[2])
    except ValueError:
        err()
    text = "".join(c for c in sys.argv[1]
                   if c not in string.punctuation).split(" ")
    tmp =[w for w in text if len(w) > size]
    len(tmp) != 0 or err()
    print(tmp)


if __name__ == "__main__":
    prout()
