# start_numbers = "0,3,6"    # test numbers
start_numbers = "0,1,4,13,15,12,16"

spoken = [int(i) for i in start_numbers.split(",")]
stop = 2020
turn = len(spoken) + 1

while turn <= stop:
    last = spoken[-1]
    print(f"Turn {turn}: \t last: {last}", end="... ")
    if spoken.count(last) == 1:
        spoken.append(0)
        print(f"fresh, 0")
    else:
        previously = len(spoken) - spoken[::-1].index(last, 1)
        spoken.append(turn - 1 - previously)
        print(f"previously {previously}, diff: {spoken[-1]}")
    turn += 1

print(f"State after turn {turn-1}:")
print(f"last spoken: {spoken[-1]}")
print("---")
# print(", ".join(str(i) for i in spoken))

