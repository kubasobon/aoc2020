import string


def apply_mask(mask, dec):
    b = bin(dec)[2:].zfill(36)
    new_b = []
    for i, v in enumerate(b):
        if mask[i] == "X":
            new_b.append(v)
            continue
        new_b.append(mask[i])
    return int("".join(new_b), 2)


test_mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
assert apply_mask(test_mask, 11) == 73
assert apply_mask(test_mask, 101) == 101
assert apply_mask(test_mask, 0) == 64


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
