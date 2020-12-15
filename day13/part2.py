with open("input.txt") as f:
    f.readline()
    conditions = {i: int(t) for i, t in enumerate(f.readline().split(",")) if t != "x"}

conditions = {0: 17, 2: 13, 3: 19}
conditions_stop = max(conditions) + 1

t = 0
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
