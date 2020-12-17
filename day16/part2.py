import string
import re
import collections


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
#     "class: 0-1 or 4-19",
#     "row: 0-5 or 8-19",
#     "seat: 0-13 or 16-19",
#     "",
#     "your ticket:",
#     "11,12,13",
#     "",
#     "nearby tickets:",
#     "3,9,18",
#     "15,1,5",
#     "5,14,9",
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


# filter out invalid tickets
valid_tickets = []

for ticket in nearby:
    for field in ticket:
        valid = any(field in rule for rule in rules.values())
        if not valid:
            break
    else:
        valid_tickets.append(ticket)

valid_tickets.append(your)

# determine field order
field_fit = {i: collections.Counter() for i in range(len(your))}
for ticket in valid_tickets:
    for i, field in enumerate(ticket):
        for name, rule in rules.items():
            if field in rule:
                field_fit[i][name] += 1

field_names = {}
while len(field_names) < len(your):
    for i, count in field_fit.items():
        # skip fields we already matched
        if i in field_names:
            continue

        mc = count.most_common()  # [("field_name", 123), ...]
        # just one name fits the position
        if len(mc) == 1 or mc[0][1] > mc[1][1]:
            name, total = mc[0]
            assert total == len(valid_tickets)
            field_names[i] = name
            continue

        # try to eliminate names
        mc = [item for item in mc if item[0] not in field_names.values()]

        if len(mc) > 1 and mc[0][1] == mc[1][1]:
            # still too many options for now, carry on
            continue

        # eliminated other options, just one fit left
        name, total = mc[0]
        assert total == len(valid_tickets)
        field_names[i] = name

result = 1
for i, value in enumerate(your):
    name = field_names[i]
    print(f"{name}: {value}")
    if name.startswith("departure"):
        result *= value

print(f"Result: {result}")
