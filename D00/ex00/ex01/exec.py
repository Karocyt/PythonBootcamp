#! /usr/bin/env python3

import sys

print("".join(c.lower() if c.isupper() else c.upper()
              for c in " ".join(sys.argv[1:])[::-1]))