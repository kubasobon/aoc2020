import string
from collections import Counter

with open("input.txt") as f:
    data = (l.strip(string.whitespace) for l in f.readlines())

total = 0

group_answers = ""
group_size = 0

for l in data:
    if l == "":
        c = Counter(group_answers)
        sub_total = sum(1 for v in c.values() if v == group_size)
        total += sub_total
        group_answers = ""
        group_size = 0
        continue
    group_answers += l
    group_size += 1

if len(group_answers) > 0:
    c = Counter(group_answers)
    total += sum(1 for v in c.values() if v == group_size)

print(f"Total questions answered 'yes' by all group members: {total}")
