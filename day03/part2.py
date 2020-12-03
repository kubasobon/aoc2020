import string


class Map:
    def __init__(self, data):
        self._map = {}
        self._width = 0
        self._height = 0
        self._ingest_data(data)

    def _ingest_data(self, data):
        assert len(data) > 0
        assert len(data[0]) > 0

        for y, row in enumerate(data):
            for x, col in enumerate(row):
                if col == "#":
                    self._map[(x, y)] = True

        self._height = len(data)
        self._width = len(data[0]) - 1

    def _normalized_coords(self, xy):
        assert isinstance(xy, tuple)
        x, y = xy
        x = x % self._width
        return (x, y)

    def __getitem__(self, k):
        k = self._normalized_coords(k)
        if k in self._map:
            return "#"
        return None

    def __contains__(self, k):
        k = self._normalized_coords(k)
        return k in self._map

    def bounds(self):
        return self._width, self._height


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [l for l in f.readlines() if l.strip(string.whitespace)]

    m = Map(data)
    w, h = m.bounds()

    subtotals = []

    for step in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        step_x, step_y = step
        x = step_x
        y = step_y

        trees_hit = 0
        while y <= h:
            if (x, y) in m:
                trees_hit += 1
            x += step_x
            y += step_y
        subtotals.append(trees_hit)

    result = 1
    for subtotal in subtotals:
        result *= subtotal
    print(f"Trees hit per step: {subtotals}")
    print(f"Product: {result}")
