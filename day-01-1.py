from math import floor
from sys import stdin

print(sum([floor(int(line) / 3) - 2 for line in stdin]))
