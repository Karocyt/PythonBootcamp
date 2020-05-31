#! /usr/bin/env python3

import time
from random import randint
import types
import logging
import getpass


logging.basicConfig(filename='machine.log',
                    format=f"({getpass.getuser()})Running: %(message)20s", level=logging.DEBUG)


def log(fun):
    def wrapper(*args, **kwargs):
        name = " ".join(s.capitalize()
                        for s in fun.__name__.split("_")).ljust(20, " ")
        try:
            start = time.time()
            ret = fun(*args, **kwargs)
            elapsed = time.time() - start
            unit = "s"
            if elapsed < 1.0:
                elapsed *= 1000
                unit = "ms"
            logging.debug(f"{name} [ exec-time = {elapsed:0.3f} {unit:2s} ]")
            return ret
        except Exception as e:
            logging.fatal(f"{name}raised an exception {type(e)}: {e}")
    if type(fun) is not types.FunctionType:
        raise ValueError()
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
