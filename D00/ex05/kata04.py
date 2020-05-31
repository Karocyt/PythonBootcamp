#! /usr/bin/env python3

t = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == "__main__":
    print(f"day_{t[0]:02d}, ex_{t[1]:02d} : "
          f"{t[2]:.3f}, {t[3]:.2e}, {t[4]:.2e}")
