import string

with open("input.txt") as f:
    bootcode = [l.strip(string.whitespace) for l in f.readlines()]

pc = 0
acc = 0
visited_pc = []

while True:
    if pc in visited_pc:
        print(f"Visited twice: {bootcode[pc]}")
        print(f"PC: {pc}")
        print(f"ACC: {acc}")
        break
    visited_pc.append(pc)

    if pc >= len(bootcode):
        print(f"PC exceeded bootcode length: {pc} >= {len(bootcode)}")
        break

    opcode, arg = bootcode[pc].split()
    arg = int(arg)

    if opcode == "acc":
        acc += arg
        pc += 1
    elif opcode == "jmp":
        pc += arg
    elif opcode == "nop":
        pc += 1
