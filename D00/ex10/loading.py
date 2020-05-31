#! /usr/bin/env python3

import time


def ft_progress(listy):
    size = 20
    start = time.time()
    for i, elem in enumerate(listy):
        elapsed = time.time() - start
        if i != 0:
            eta = elapsed*len(listy)/i - elapsed
            eta = f"ETA: {eta:.2f}s"
        else:
            eta = "          "
        print(f"{eta} [{int(i/len(listy)): 3}%] [" +
              ">".rjust(max(0, int(i/len(listy)*size)+1), '=').ljust(
                  size, ' ') +
              f"] {i}/{len(listy)} | elapsed time {elapsed:.2}s",
              end="\r", flush=True)
        yield elem


if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)
