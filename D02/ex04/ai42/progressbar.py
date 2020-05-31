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
        print(f"{eta:11s} [{int((i+1)/len(listy)*100):3d}%] [" +
              ">".rjust(max(0, int((i+1)/len(listy)*size)), '=').ljust(
                  size, ' ') +
              f"] {(i+1): 3d}/{len(listy)} | elapsed time {elapsed:.2f}s          ",
              end="\r", flush=True)
        yield elem

