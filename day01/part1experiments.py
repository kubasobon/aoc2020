import string
import time


def unoptimized(data):
    for a in data:
        for b in data:
            if a + b == 2020:
                return a, b, a * b
    return None, None, None


def optimized(data):
    for a in sorted(data):
        for b in sorted(data, reverse=True):
            result = a + b
            if result > 2020:
                continue
            elif result < 2020:
                break
            return a, b, a * b
    return None, None, None


def timeit(iterations, func, *args, **kwargs):
    avg = 0.0
    for _ in range(iterations):
        start = time.time_ns()
        result = func(*args, **kwargs)
        avg += float(time.time_ns() - start)
    avg = (avg / iterations) / 1000000
    print(f"Ran {func.__name__} {iterations} times: average time was {avg:.3f}s")
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [int(l) for l in f.readlines() if l.strip(string.whitespace)]

    a, b, ab = timeit(1000, unoptimized, data)
    print(f"a: {a}, b: {b}, a*b: {a*b}")

    a, b, ab = timeit(1000, optimized, data)
    print(f"a: {a}, b: {b}, a*b: {a*b}")
