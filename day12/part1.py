import math

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
s.fwd(10)
s.move_n(3)
s.fwd(7)
s.turn_r(90)
s.fwd(11)

print(f"x: {s.x}, y: {s.y}")
manhattan = abs(s.x) + abs(s.y)
print(f"Manhattan distance from zero: {manhattan}")
