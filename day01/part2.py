import sys
import string

with open("input.txt") as f:
    data = [int(l) for l in f.readlines() if l.strip(string.whitespace)]

asc = sorted(data)
for a in asc:
    for b in asc:
        c = 2020 - a - b
        if c <= 0:
            continue
        if c in asc:
            print(f"a: {a}, b: {b}, c: {c}, a*b*c: {a*b*c}")
            sys.exit()

print("Condition has not been met")
