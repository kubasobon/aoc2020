import string

from timer import timefunc


def unoptimized(data):
    for a in data:
        for b in data:
            if a + b == 2020:
                return a, b, a * b
    return None, None, None


def optimized_nested(data):
    for a in sorted(data):
        for b in sorted(data, reverse=True):
            result = a + b
            if result > 2020:
                continue
            elif result < 2020:
                break
            return a, b, a * b
    return None, None, None


def optimized_lookup(data):
    for a in sorted(data):
        b = 2020 - a
        if b in data:
            return a, b, a * b
    return None, None, None


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [int(l) for l in f.readlines() if l.strip(string.whitespace)]

    a, b, ab = timefunc(1000, unoptimized, data)
    print(f"a: {a}, b: {b}, a*b: {a*b}")

    a, b, ab = timefunc(1000, optimized_nested, data)
    print(f"a: {a}, b: {b}, a*b: {a*b}")

    a, b, ab = timefunc(1000, optimized_lookup, data)
    print(f"a: {a}, b: {b}, a*b: {a*b}")
