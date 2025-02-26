#! /usr/bin/env python3

import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

if __name__ == "__main__":
    ret = ""
    try:
        for c in " ".join(sys.argv[1:]):
            if c == '/':
                raise Exception()
            elif c == ' ':
                ret += '/'
            else:
                ret += MORSE_CODE_DICT[c.upper()]
            ret += " "
        if len(ret) > 0:
            ret = ret[:-1]
        print(ret)
    except Exception as e:
        print("ERROR", e)
        sys.exit(1)
