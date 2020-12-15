with open("input.txt") as f:
    f.readline()
    conditions = {i: int(t) for i, t in enumerate(f.readline().split(",")) if t != "x"}

t = 0
while True:
    match = True
    for i, key in enumerate(conditions):
        if (t + i) % conditions[key] > 0:
            match = False
            break
    if match:
        print(f"Matched positions at {t}")
        break
    t += 1
