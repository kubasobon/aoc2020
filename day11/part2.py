import string


with open("input.txt") as f:
    data = [l.strip(string.whitespace) for l in f.readlines()]

directions = (
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1),
)

def trace(state, x, y, dx, dy, max_x, max_y):
    while True:
        x += dx
        y += dy
        if x >= max_x or y >= max_y:
            return False
        if x <= 0 or y <= 0:
            return False
        if state[y][x] == "#":
            return True


def next_state(state):
    rows = len(state)
    cols = len(state[0])
    future = []

    for y, row in enumerate(state):
        for x, ch in enumerate(row):
            row = []
            if ch == ".":
                row.append(ch)
                continue
            taken = 0
            for d in directions:
                dx, dy = d
                if trace(state, x, y, dx, dy, cols, rows):
                    taken += 1

            if ch == "#" and taken >= 5:
                row.append("L")
            elif ch == "L" and taken == 0:
                row.append("#")
            else:
                row.append(ch)
        future.append(row)
    return future

def flattened(state):
    return "".join("".join(l) for l in state)

with open("input.txt") as f:
    state = [l.strip(string.whitespace) for l in f.readlines()]

prev_state = []
iterations = 0

while flattened(prev_state) != flattened(state):
    prev_state = state
    state = future_state(state)
    iterations += 1

print(f"Stable after {iterations} iterations")
seats_occupied = state.count("#")
print(f"Occupied seats: {seats_occupied}")



