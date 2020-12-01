import sys
import string

with open("input.txt") as f:
    data = [int(l) for l in f.readlines() if l.strip(string.whitespace)]

lookup = {}.fromkeys(data)
for a in data:
    b = 2020 - a
    if b in lookup:
        print(f"a: {a}, b: {b}, a*b: {a*b}")
        sys.exit()

print("Condition has not been met")
