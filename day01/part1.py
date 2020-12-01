import sys
import string

with open("input.txt") as f:
    data = [int(l) for l in f.readlines() if l.strip(string.whitespace)]

for a in sorted(data):
    b = 2020 - a
    if b in data:
        print(f"a: {a}, b: {b}, a*b: {a*b}")
        sys.exit()

print("Condition has not been met")
