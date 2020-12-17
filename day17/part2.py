from functools import lru_cache
from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int
    z: int
    w: int

    def __hash__(self):
        return hash((self.x, self.y, self.z, self.w))


@lru_cache(maxsize=1_000_000)
def new_state(state, *neighbors):
    s = sum(neighbors)
    # active
    if state == 1:
        if s == 2 or s == 3:
            return 1
        return 0
    # inactive
    if s == 3:
        return 1
    return 0


def bounds(world):
    min_x, min_y, min_z, min_w = 0, 0, 0, 0
    max_x, max_y, max_z, max_w = 0, 0, 0, 0
    for coords in world:
        x, y, z, w = coords.x, coords.y, coords.z, coords.w
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        min_w = min(min_w, w)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)
        max_w = max(max_w, w)
    return (
        Coordinates(min_x, min_y, min_z, min_w),
        Coordinates(max_x, max_y, max_z, max_w),
    )


@lru_cache(maxsize=1_000_000)
def neighbor_coords(coords):
    x0, y0, z0, w0 = coords.x, coords.y, coords.z, coords.w
    c = []
    for w in range(w0 - 1, w0 + 2):
        for z in range(z0 - 1, z0 + 2):
            for y in range(y0 - 1, y0 + 2):
                for x in range(x0 - 1, x0 + 2):
                    if x == x0 and y == y0 and z == z0 and w == w0:
                        continue
                    c.append(Coordinates(x, y, z, w))
    return c


def tick(world):
    new_world = {}
    mini, maxi = bounds(world)
    for w in range(mini.w - 1, maxi.w + 2):
        for z in range(mini.z - 1, maxi.z + 2):
            for y in range(mini.y - 1, maxi.y + 2):
                for x in range(mini.x - 1, maxi.x + 2):
                    c = Coordinates(x, y, z, w)
                    neighbor_states = [
                        world[nc] if nc in world else 0 for nc in neighbor_coords(c)
                    ]
                    ns = new_state(world[c] if c in world else 0, *neighbor_states)
                    if ns == 1:
                        new_world[c] = 1
    return new_world


world = {}
with open("input.txt") as f:
    for y, l in enumerate(reversed(f.readlines())):
        for x, ch in enumerate(l):
            if ch == "#":
                c = Coordinates(x, y, 0, 0)
                world[c] = 1

for t in range(6):
    print(f"Tick {t+1}...")
    world = tick(world)

print(f"Active cubes: {sum(world.values())}")
