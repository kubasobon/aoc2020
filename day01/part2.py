import sys
import string

with open("input.txt") as f:
    data = [int(l) for l in f.readlines() if l.strip(string.whitespace)]

asc = sorted(data)

for a in asc:
    for b in asc:
        for c in asc:
            if a + b + c == 2020:
                print(f"a: {a}, b: {b}, c: {c}, a*b*c: {a*b*c}")
                sys.exit()

print("Condition has not been met")
