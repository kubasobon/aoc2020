import string

with open("input.txt") as f:
    bootcode = (l.strip(string.whitespace) for l in f.readlines())

breakpoint()
