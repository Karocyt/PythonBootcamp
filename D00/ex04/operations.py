#! /usr/bin/env python3

import sys


class InputError(Exception):
    pass


USAGE = (f"usage: {sys.argv[0]} <number1> <number2>\n"
         f"Example:\n\tpython operations.py 10 3")


def prog(*args):
    if len(args) is 1:
        raise InputError("not enough arguments")
    elif len(args) > 2:
        raise InputError("too many arguments")

    try:
        nb1, nb2 = int(args[0]), int(args[1])
    except ValueError:
        raise InputError("only numbers")

    def getDiv(nb1, nb2):
        try:
            return nb1 / nb2
        except ZeroDivisionError:
            return "ERROR (div by zero)"

    def getMod(nb1, nb2):
        try:
            return nb1 % nb2
        except ZeroDivisionError:
            return "ERROR (modulo by zero)"

    print(f"Sum:\t\t{nb1 + nb2}\n"
          f"Difference:\t{abs(nb1 - nb2)}\n"
          f"Product:\t{nb1 * nb2}\n"
          f"Sum:\t\t{getDiv(nb1, nb2)}\n"
          f"Sum:\t\t{getMod(nb1, nb2)}\n")


if __name__ == "__main__":
    if len(sys.argv) is 1:
        print(USAGE)
        sys.exit(1)
    try:
        prog(*sys.argv[1:])
    except Exception as e:
        print(f"InputError: {e}", type(e))
        print()
        print(USAGE)
        sys.exit(1)
