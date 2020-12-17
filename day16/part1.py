import string
import re


class Range:
    def __init__(self, *args):
        assert len(args) % 2 == 0
        args = sorted(int(i) for i in args)
        self.__ranges = tuple(
            range(args[i], args[i + 1] + 1) for i in range(0, len(args), 2)
        )

    def __contains__(self, num):
        return any(num in r for r in self.__ranges)


with open("input.txt") as f:
    data = [l.strip(string.whitespace) for l in f]

# test data
# data = [
#     "class: 1-3 or 5-7",
#     "row: 6-11 or 33-44",
#     "seat: 13-40 or 45-50",
#     "",
#     "your ticket:",
#     "7,1,14",
#     "",
#     "nearby tickets:",
#     "7,3,47",
#     "40,4,50",
#     "55,2,20",
#     "38,6,12",
# ]

# pre-parsing
sep = data.index("")
raw_rules = data[:sep]

sep2 = data.index("", sep + 1)
raw_your = data[sep + 1 : sep2][1]

raw_nearby = data[sep2 + 1 :][1:]

# parsing
num_pattern = re.compile(r"(\d+)")
rules = {}
for rr in raw_rules:
    name, definition = rr.split(":")
    numbers = num_pattern.findall(definition)
    rules[name] = Range(*numbers)

your = [int(i) for i in raw_your.split(",")]

nearby = []
for l in raw_nearby:
    nearby.append([int(i) for i in l.split(",")])


# calculate error rate
errors = []

for ticket in nearby:
    for field in ticket:
        valid = any(field in rule for rule in rules.values())
        if not valid:
            errors.append(field)

print(f"Errors: {errors}")
print(f"Error rate: {sum(errors)}")
