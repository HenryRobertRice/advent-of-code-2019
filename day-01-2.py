from math import floor
from sys import stdin

def main():
    print(sum([fuel(line) for line in stdin]))

def fuel(n):
    fuel = floor(int(n) / 3) - 2
    next_fuel = floor(int(fuel) / 3) - 2
    while next_fuel > 0:
        fuel += next_fuel
        next_fuel = floor(int(next_fuel) / 3) - 2
    return fuel

if __name__ == "__main__":
    main()
