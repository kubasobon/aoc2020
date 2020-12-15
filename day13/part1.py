with open("input.txt") as f:
    arrival = int(f.readline())
    bus_ids = [int(b) for b in f.readline().split(",") if b.isdigit()]

# time to departure
min_ttd = arrival + 1
bus_id = 0

for b in bus_ids:
    ttd = arrival % b
    if ttd < min_ttd:
        min_ttd = ttd
        bus_id = b

print(f"Bus ID: {bus_id}, To Departure: {min_ttd}")
print(f"Result: {bus_id * min_ttd}")
