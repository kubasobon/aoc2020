import functools


with open("input.txt") as f:
    adapters = sorted(int(l) for l in f.readlines())

device = max(adapters) + 3
adapters.append(0)


@functools.lru_cache(maxsize=len(adapters) + 1)
def count_combinations_downwards(joltage):
    if joltage == 0:
        return 1

    total = 0
    for j in (joltage - 1, joltage - 2, joltage - 3):
        if j not in adapters:
            continue
        total += count_combinations_downwards(j)

    return total


print(f"Counting valid combinations of {len(adapters)-1} adapters")
result = count_combinations_downwards(device)
print(f"Combinations: {result}")
