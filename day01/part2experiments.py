import string

from timer import timefunc


def unoptimized(data):
    for a in data:
        for b in data:
            for c in data:
                if a + b + c == 2020:
                    return a, b, c, a * b * c
    return None, None, None, None


def optimized(data):
    asc = sorted(data)
    for a in asc:
        for b in asc:
            for c in asc:
                if a + b + c == 2020:
                    return a, b, c, a * b * c
    return None, None, None, None


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [int(l) for l in f.readlines() if l.strip(string.whitespace)]

    a, b, c, abc = timefunc(100, unoptimized, data)
    print(f"a: {a}, b: {b}, c: {c}, a*b*c: {abc}")

    a, b, c, abc = timefunc(100, optimized, data)
    print(f"a: {a}, b: {b}, c: {c}, a*b*c: {abc}")
