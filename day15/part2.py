class Mentions:
    def __init__(self, start):
        self.latest = {int(x): i+1 for i, x in enumerate(start)}
        self.prev = {}

    def is_first(self, i):
        return i in self.latest and i not in self.prev

    def get_next(self, i):
        if self.is_first(i):
            return 0
        else:
            return self.latest[i] - self.prev[i]

    def speak(self, turn, i):
        if i in self.latest:
            self.prev[i] = self.latest[i]
        self.latest[i] = turn


start_numbers = "0,1,4,13,15,12,16"
# start_numbers = "0,3,6"    # test numbers

sn = [int(x) for x in start_numbers.split(",")]
mentions = Mentions(sn)
stop = 30_000_000
turn = len(mentions.latest) + 1
last = sn[-1]

while turn <= stop:
    n = mentions.get_next(last)
    mentions.speak(turn, n)
    # print(f"Turn {turn}: \t last: {last}, next: {n}")
    last = n
    turn += 1

print(f"State after turn {turn-1}:")
print(f"last spoken: {last}")

