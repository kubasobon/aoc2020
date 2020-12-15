with open("input.txt") as f:
    f.readline()
    raw_conditions = enumerate(f.readline().split(","))

t = 0
jmp = 1
for i, b in raw_conditions:
    if b == "x":
        continue

    while (t + i) % int(b) != 0:
        t += jmp

    jmp *= int(b)

print(f"Result: {t}")
