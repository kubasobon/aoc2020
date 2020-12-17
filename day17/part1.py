from functools import lru_cache
from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int
    z: int

    def __hash__(self):
        return hash((self.x, self.y, self.z))


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
    min_x, min_y, min_z = 0, 0, 0
    max_x, max_y, max_z = 0, 0, 0
    for coords in world:
        x, y, z = coords.x, coords.y, coords.z
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)
    return (
        Coordinates(min_x, min_y, min_z),
        Coordinates(max_x, max_y, max_z),
    )


@lru_cache(maxsize=1_000_000)
def neighbor_coords(coords):
    x0, y0, z0 = coords.x, coords.y, coords.z
    c = []
    for z in range(z0 - 1, z0 + 2):
        for y in range(y0 - 1, y0 + 2):
            for x in range(x0 - 1, x0 + 2):
                if x == x0 and y == y0 and z == z0:
                    continue
                c.append(Coordinates(x, y, z))
    return c


def tick(world):
    new_world = {}
    mini, maxi = bounds(world)
    for z in range(mini.z - 1, maxi.z + 2):
        for y in range(mini.y - 1, maxi.y + 2):
            for x in range(mini.x - 1, maxi.x + 2):
                c = Coordinates(x, y, z)
                neighbor_states = [
                    world[nc] if nc in world else 0 for nc in neighbor_coords(c)
                ]
                ns = new_state(world[c] if c in world else 0, *neighbor_states)
                if ns == 1:
                    new_world[c] = 1
    return new_world


world = {
    Coordinates(0, 0, 0): 1,
    Coordinates(1, 0, 0): 1,
    Coordinates(2, 0, 0): 1,
    Coordinates(2, 1, 0): 1,
    Coordinates(1, 2, 0): 1,
}

for t in range(6):
    print(f"Tick {t+1}...")
    world = tick(world)

print(f"Active cubes: {sum(world.values())}")
