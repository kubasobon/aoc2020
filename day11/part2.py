import string


def future_state(state, row_len):
    future = []
    translations = (
        -row_len - 1,
        -row_len,
        -row_len + 1,
        -1,
        1,
        row_len - 1,
        row_len,
        row_len + 1,
    )
    for i, ch in enumerate(state):
        if ch == ".":
            future.append(ch)
            continue

        adjacent_occupied = 0
        for tidx, t in enumerate(translations):
            check = i + t
            if check < 0 or check >= len(state):
                continue  # total limits
            if i % row_len == 0 and tidx in (0, 3, 5):
                continue  # left
            if i % row_len == row_len - 1 and tidx in (2, 4, 7):
                continue  # right
            if state[check] == "#":
                adjacent_occupied += 1

        if ch == "L" and adjacent_occupied == 0:
            future.append("#")
        elif ch == "#" and adjacent_occupied >= 4:
            future.append("L")
        else:
            future.append(ch)

    return "".join(future)


with open("input.txt") as f:
    data = [l.strip(string.whitespace) for l in f.readlines()]

row_len = len(data[0])
state = "".join(data)
prev_state = ""
iterations = 0

while prev_state != state:
    prev_state = state
    # for i, ch in enumerate(state):
    #     if i % row_len == 0 and i > 0:
    #         print("")
    #     print(ch, end="")
    # print("\n---")
    state = future_state(state, row_len)
    iterations += 1

print(f"Stable after {iterations} iterations")
seats_occupied = state.count("#")
print(f"Occupied seats: {seats_occupied}")
