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
        if x < 0 or y < 0:
            return False
        if state[y][x] == "#":
            return True
        if state[y][x] == "L":
            return False


def next_state(state):
    rows = len(state)
    cols = len(state[0])
    future = []

    for y, row in enumerate(state):
        frow = []
        for x, ch in enumerate(row):
            if ch == ".":
                frow.append(ch)
                continue

            taken = 0

            for d in directions:
                dx, dy = d
                if trace(state, x, y, dx, dy, cols, rows):
                    taken += 1

            if ch == "#" and taken >= 5:
                frow.append("L")
            elif ch == "L" and taken == 0:
                frow.append("#")
            else:
                frow.append(ch)

        future.append("".join(frow))
    return future

def flattened(state):
    return "".join(state)

with open("input.txt") as f:
    state = [l.strip(string.whitespace) for l in f.readlines()]


state = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL",
]


prev_state = []
iterations = 0

while prev_state != flattened(state):
    prev_state = flattened(state)
    state = next_state(state)
    iterations += 1

print(f"Stable after {iterations} iterations")
seats_occupied = sum(l.count("#") for l in state)
print(f"Occupied seats: {seats_occupied}")



