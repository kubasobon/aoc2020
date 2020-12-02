import time


def timefunc(iterations, func, *args, **kwargs):
    avg = 0.0
    for _ in range(iterations):
        start = time.time_ns()
        result = func(*args, **kwargs)
        avg += float(time.time_ns() - start)
    # Divide by a billion to translate nanoseconds to seconds
    avg = (avg / iterations) / 1_000_000_000
    print(f"Ran {func.__name__} {iterations} times: average time was {avg:.5f}s")
    return result
