with open("input.txt") as f:
    data = [int(i) for i in f.readlines()]


preamble_len = 25
pos = preamble_len
results = {}

while pos < len(data):
    numbers = {}.fromkeys(data[pos-preamble_len:pos])
    key = data[pos]

    match = False
    for n in numbers:
        n2 = key - n
        if n2 == n:
            continue
        if n2 in numbers:
            break
    else:
        print(f"Could not factor key: {key} at position: {pos}")
        break

    pos += 1
