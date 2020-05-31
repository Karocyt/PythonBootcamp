#! /usr/bin/env python3

import random
import sys

if __name__ == "__main__":
    print("This is an interactive guessing game!\n"
          "You have to enter a number between 1 and 99 "
          "to find out the secret number.\n"
          "Type 'exit' to end the game.\n"
          "Good luck!\n")
    guess = -1
    to_guess = random.randint(1, 99)
    tries = 0
    while guess is not to_guess:
        tries += 1
        txt = input("What's your guess between 1 and 99?\n")
        if txt == "exit":
            print("See ya!")
            sys.exit(0)
        try:
            guess = int(txt)
            if guess < 1 or guess > 99:
                raise Exception
        except Exception:
            print("This is not a valid number.")
            continue
        if guess < to_guess:
            print("Too low.")
        elif guess > to_guess:
            print("Too high.")
        else:
            print("Right on!")
            if tries == 1:
                print("And from the first shot, congrats!")
            else:
                print(f"In {tries} tries, not that bad.")
            if to_guess == 42:
                print("The answer to the ultimate question of life, "
                      "the universe and everything is 42.")
