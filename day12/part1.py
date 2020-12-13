import math
import string


class Ship:
    x = 0
    y = 0
    angle = 0.0

    def move_n(self, v):
        self.y += v

    def move_s(self, v):
        self.y -= v

    def move_e(self, v):
        self.x += v

    def move_w(self, v):
        self.x -= v

    def turn_l(self, angle):
        self.angle += angle
        self.angle = self.angle % 360

    def turn_r(self, angle):
        self.angle -= angle
        self.angle = self.angle % 360

    def fwd(self, v):
        if self.angle < 90:
            angle = math.radians(self.angle)
            dx = v * math.cos(angle)
            dy = dx * math.tan(angle)
        elif self.angle == 90:
            self.y += v
            return
        elif self.angle < 180:
            angle = math.radians(self.angle - 90.0)
            dy = v * math.cos(angle)
            dx = -1 * dy * math.tan(angle)
        elif self.angle == 180:
            self.x -= v
            return
        elif self.angle < 270:
            angle = math.radians(self.angle - 180)
            dx = -1 * v * math.cos(angle)
            dy = -1 * dx * math.tan(angle)
        elif self.angle == 270:
            self.y -= v
            return
        elif self.angle < 360:
            angle = math.radians(self.angle - 270)
            dy = -1 * v * math.cos(angle)
            dx = dy * math.tan(angle)
        elif self.angle == 0 or self.angle == 360:
            self.x += v
            return
        else:
            raise ValueError

        self.x += dx
        self.y += dy


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


print(f"x: {s.x}, y: {s.y}")
manhattan = abs(s.x) + abs(s.y)
print(f"Manhattan distance from zero: {manhattan}")
