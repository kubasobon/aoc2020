import sys
import string

with open("input.txt") as f:
    data = [int(l) for l in f.readlines() if l.strip(string.whitespace)]

for a in sorted(data):
    for b in sorted(data, reverse=True):
        if a + b == 2020:
            print(f"a: {a}, b: {b}, a*b: {a*b}")
            sys.exit()

print("Condition has not been met")
