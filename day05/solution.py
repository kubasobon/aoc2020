import string


def bisect_low(range_):
    mid = (range_.stop - range_.start) // 2
    return range(range_.start, range_.start + mid)


def bisect_high(range_):
    mid = (range_.stop - range_.start) // 2
    return range(range_.start + mid, range_.stop)


def seat_id(boarding_pass):
    row_selector = boarding_pass[:7]
    col_selector = boarding_pass[7:]

    row = 0
    rng = range(0, 128)
    for high_low in row_selector:
        if high_low == "F":
            rng = bisect_low(rng)
        elif high_low == "B":
            rng = bisect_high(rng)
        else:
            raise Exception("Invalid selector")
        # print(f"{high_low}: {rng.start}, {rng.stop}")
    row = rng.start

    col = 0
    rng = range(0, 8)
    for high_low in col_selector:
        if high_low == "L":
            rng = bisect_low(rng)
        elif high_low == "R":
            rng = bisect_high(rng)
        else:
            raise Exception("Invalid selector")
    col = rng.start

    return row * 8 + col


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [l.strip(string.whitespace) for l in f.readlines()]

    seat_ids = [seat_id(bp) for bp in data]
    max_id = max(seat_ids)
    print(f"Highest sit ID: {max_id}")

    empty_seats = ", ".join([str(s) for s in range(max_id) if s not in seat_ids])
    print(f"Empty seat ids: {empty_seats}")
