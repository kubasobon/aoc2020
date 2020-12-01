import string
import time


def unoptimized(data):
    for a in data:
        for b in data:
            for c in data:
                if a + b + c == 2020:
                    return a, b, c, a*b*c
    return None, None, None, None


def optimized(data):
    asc = sorted(data)
    for a in asc:
        for b in asc:
            for c in asc:
                if a + b + c == 2020:
                    return a, b, c, a*b*c
    return None, None, None, None


def timeit(iterations, func, *args, **kwargs):
    avg = 0.0
    for _ in range(iterations):
        start = time.time_ns()
        result = func(*args, **kwargs)
        avg += float(time.time_ns() - start)
    avg = (avg / iterations) / 1000000000
    print(f"Ran {func.__name__} {iterations} times: average time was {avg:.5f}s")
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [int(l) for l in f.readlines() if l.strip(string.whitespace)]

    a, b, c, abc = timeit(100, unoptimized, data)
    print(f"a: {a}, b: {b}, c: {c}, a*b*c: {abc}")

    a, b, c, abc = timeit(100, optimized, data)
    print(f"a: {a}, b: {b}, c: {c}, a*b*c: {abc}")
