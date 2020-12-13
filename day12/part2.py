import math
import string


class Ship:
    x = 0
    y = 0
    way_x = 10
    way_y = 1

    def move_n(self, v):
        self.way_y += v

    def move_s(self, v):
        self.way_y -= v

    def move_e(self, v):
        self.way_x += v

    def move_w(self, v):
        self.way_x -= v

    def turn_l(self, da):
        sin = math.sin(math.radians(da))
        cos = math.cos(math.radians(da))
        wx = self.way_x * cos - self.way_y * sin
        wy = self.way_y * cos + self.way_x * sin
        self.way_x = int(wx)
        self.way_y = int(wy)

    def turn_r(self, da):
        self.turn_l(-da)

    def fwd(self, v):
        self.x += v * self.way_x
        self.y += v * self.way_y


s = Ship()
funcmap = {
    "N": s.move_n,
    "S": s.move_s,
    "E": s.move_e,
    "W": s.move_w,
    "F": s.fwd,
    "R": s.turn_r,
    "L": s.turn_l,
}


with open("input.txt") as f:
    for line in (l.strip(string.whitespace) for l in f.readlines()):
        cmd = line[0]
        arg = int(line[1:])

        funcmap[cmd](arg)
        # print(f"{line}\tx: {s.x}, y: {s.y}, wx: {s.way_x}, wy: {s.way_y}")


manhattan = abs(s.x) + abs(s.y)
print(f"Manhattan distance from zero: {manhattan}")
