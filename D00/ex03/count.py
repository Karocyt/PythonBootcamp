#! /usr/bin/env python3

import string


def text_analyzer(*args):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text. No, it doesn't care about any '\\n'."""
    if len(args) > 1:
        print("ERROR")
        return
    if len(args) is 1:
        text = args[0]
    else:
        text = input("What is the text to analyse?\n")

    chars = len(text)
    uppers = sum(1 for c in text if c.isupper())
    lowers = sum(map(str.islower, text))
    punc = sum(1 for c in text if c in string.punctuation)
    spaces = text.count(" ")
    print(
        f"The text contains {chars} characters:\n\n"
        "- {uppers} upper letters\n\n"
        "- {lowers} lower letters\n\n"
        "- {punc} punctuation marks\n\n"
        "- {spaces} spaces")
