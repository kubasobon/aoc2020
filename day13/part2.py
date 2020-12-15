with open("input.txt") as f:
    f.readline()
    raw_conditions = enumerate(f.readline().split(","))

conditions = {
    int(c): int(c) - (i % int(c)) if i > 0 else 0 for i, c in raw_conditions if c != "x"
}

print(f"Conditions: {conditions}")


while True:
    match = True
    for i in range(conditions_stop):
        if i not in conditions:
            continue
        if (t + i) % conditions[i] > 0:
            match = False
            break
    if match:
        print(f"Matched positions at {t}")
        break
    t += 1
    if t % 1_000_000 == 0:
        print(f"t = {t}")
