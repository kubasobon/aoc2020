with open("input.txt") as f:
    f.readline()
    raw_conditions = enumerate(f.readline().split(","))

conditions = {
    int(c): int(c) - (i % int(c)) if i > 0 else 0 for i, c in raw_conditions if c != "x"
}

conditions = {67: 0, 7: 6, 59: 57, 61: 58}
conditions = {1789: 0, 37: 37 - 1, 47: 47 - 2, 1889: 1889 - 3}
print(f"Conditions: {conditions}")

t = max(conditions)
jmp = 0
for k, v in conditions.items():
    if k < t and v == 0:
        t = k
        jmp = k


print(f"t: {t}, jmp: {jmp}")
while True:
    if not all(t % k == v for k, v in conditions.items()):
        t += jmp
        continue
    print(f"Matched positions at {t}")
    break
