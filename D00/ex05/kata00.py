#! /usr/bin/env python3

t = (19, 42, 21)

if __name__ == "__main__":
    print(f"The {len(t)} numbers are: "
          ", ".join(str(n) for n in t))
