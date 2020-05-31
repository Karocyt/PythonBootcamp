#! /usr/bin/env python3

class GotCharacter:
    """A class template for GoT characters"""

    def __init__(self, name: str, is_alive: bool = True):
        self.name = name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class for the Stark family. When bad things happen to good people."""
    family_name = "Stark"
    house_words = "Winter is Coming"

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(name=first_name, is_alive=is_alive)

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


if __name__ == "__main__":
    sansa = Stark(325)
    print(sansa.name)
    arya = Stark("Arya")
    print(arya.__dict__)
    arya.print_house_words()
    print(arya.is_alive)
    arya.die()
    print(arya.is_alive)
    print(arya.__doc__)
