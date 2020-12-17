from functools import lru_cache
from dataclasses import dataclass

@dataclass
class Coordinates:
    x: int
    y: int
    z: int

    def __hash__(self):
        return hash((self.x, self.y, self.z))

@lru_cache(max_size=1_000_000)
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

@lru_cache(max_size=1_000_000)
def neighbor_coords(coords):
    x, y, z = coords.x, coords.y, coords.z
    c = []
    for z in range(z-1, z+2):
        for y in range(y-1, y+2):
            for x in range(x-1, x+2):
                c.append(Coordinates(x, y, z))
    return c

def tick(world):
    new_world = {}
    mini, maxi = bounds(world)
    for z in range(mini.z, maxi.z+1):
        for y in range(mini.y, maxi.y+1):
            for x in range(mini.x, maxi.x+1):
                c = Coordinates(x, y, z)
                neighbor_states = [
                    world[nc] if nc in world else 0
                    for nc in neighbor_coords(c)
                ]
                new_world[c] = new_state(
                    world[c] if c in world else 0,
                    *neighbor_states
                )
    return new_world

