import string


def apply_mask(mask, dec):
    b = bin(dec)[2:].zfill(36)
    new_b = []
    for i, v in enumerate(mask):
        if v == "X":
            new_b.append(b[i])
            continue
        new_b.append(v)
    return int(b, 2)


with open("input.txt") as f:
    data = [l.strip(string.whitespace) for l in f.readlines()]

mask = ""
mem = {}
for l in data:
    if l.startswith("mask"):
        mask = l.split(" = ")[1]
        continue
    mem_prefix, v = l.split(" = ")
    v = apply_mask(mask, int(v))
    address = int(mem_prefix.strip("me[]"))
    mem[address] = v


print("--- memory ---")
for k, v in mem.items():
    print(f"{k}:\t{v}")
print("--------------")

result = sum(mem.values())
print(f"Sum of memory values: {result}")
