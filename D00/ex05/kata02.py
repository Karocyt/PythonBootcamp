#! /usr/bin/env python3

from datetime import datetime as dt

t = (3, 30, 2019, 9, 25)

if __name__ == "__main__":
    print(dt.strftime(dt.strptime(
        " ".join(str(nb) for nb in t), "%H %M %Y %m %d"), "%m/%d/%Y %H:%M"))
