import string
import itertools


def apply_mask(mask, dec):
    b = bin(dec)[2:].zfill(36)
    variants = itertools.product("01", repeat=mask.count("X"))
    results = []

    for variant in variants:
        new_b = []
        x = 0
        for i, v in enumerate(b):
            if mask[i] == "0":
                new_b.append(v)
            elif mask[i] == "1":
                new_b.append("1")
            else:
                new_b.append(variant[x])
                x += 1
        results.append(int("".join(new_b), 2))

    return results


test_mask = "00000000000000000000000000000000X0XX"
assert apply_mask(test_mask, 26) == [16, 17, 18, 19, 24, 25, 26, 27]


with open("input.txt") as f:
    data = [l.strip(string.whitespace) for l in f.readlines()]

mask = ""
mem = {}
for l in data:
    if l.startswith("mask"):
        mask = l.split(" = ")[1]
        continue
    mem_prefix, v = l.split(" = ")
    address = int(mem_prefix.strip("me[]"))
    for a in apply_mask(mask, address):
        mem[a] = int(v)


# print("--- memory ---")
# for k, v in mem.items():
#     print(f"{k}:\t{v}")
# print("--------------")

result = sum(mem.values())
print(f"Sum of memory values: {result}")
