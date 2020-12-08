import string
import sys

with open("input.txt") as f:
    bootcode = [l.strip(string.whitespace) for l in f.readlines()]


# test_bootcode = [
#     "nop +0",
#     "acc +1",
#     "jmp +4",
#     "acc +3",
#     "jmp -3",
#     "acc -99",
#     "acc +1",
#     "jmp -4",
#     "acc +6",
# ]
# bootcode = test_bootcode


for change_pc in range(len(bootcode) - 1, -1, -1):
    if bootcode[change_pc].startswith("acc"):
        continue

    pc = 0
    acc = 0
    visited_pc = []
    while True:
        if pc in visited_pc:
            break  # infinite loop
        visited_pc.append(pc)

        if pc == len(bootcode):
            print(f"Bootcode terminated correctly")
            print(f"Changed opcode at: {change_pc}")
            print(f"PC: {pc}")
            print(f"ACC: {acc}")
            sys.exit()

        opcode, arg = bootcode[pc].split()
        arg = int(arg)

        if pc == change_pc:
            if opcode == "jmp":
                opcode = "nop"
            elif opcode == "nop":
                opcode = "jmp"

        if opcode == "acc":
            acc += arg
            pc += 1
            continue
        if opcode == "jmp":
            pc += arg
            continue
        if opcode == "nop":
            pc += 1
            continue
