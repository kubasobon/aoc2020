with open("input.txt") as f:
    data = sorted(int(l) for l in f.readlines())


socket = 0
data.append(max(data) + 3)  # add device to the chain

differences = {1: 0, 2: 0, 3: 0}
current_output = socket
for adapter in data:
    diff = adapter - current_output
    assert diff < 4
    differences[diff] += 1
    current_output = adapter

assert differences[2] == 0
print(f"Result: {differences[1]*differences[3]}")
