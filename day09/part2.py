import sys


with open("input.txt") as f:
    data = [int(i) for i in f.readlines()]


key = 31161678
for start in range(len(data)):
    pos = start
    total = 0
    while pos < len(data):
        total += data[pos]
        if total == key:
            print(f"Found contiguous range: {start}:{pos+1}")
            numbers = data[start : pos + 1]
            assert sum(numbers) == key
            low = min(numbers)
            high = max(numbers)
            print(f"Min: {low}, Max: {high}, Sum: {low+high}")
            sys.exit()
        elif total > key:
            break
        pos += 1
