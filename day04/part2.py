import string

required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")  # , "cid")
eye_colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def validate(fields):
    if any(rf not in fields for rf in required_fields):
        return False

    byr = int(fields["byr"])
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(fields["iyr"])
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(fields["eyr"])
    if eyr < 2020 or eyr > 2030:
        return False

    if fields["hgt"].endswith("cm"):
        try:
            hgt = int(fields["hgt"][:-2])
        except ValueError:
            return False
        if hgt < 150 or hgt > 193:
            return False
    elif fields["hgt"].endswith("in"):
        try:
            hgt = int(fields["hgt"][:-2])
        except ValueError:
            return False
        if hgt < 59 or hgt > 76:
            return False
    else:
        return False

    if len(fields["hcl"]) != 7 or fields["hcl"][0] != "#":
        return False
    hcl = fields["hcl"][1:]
    if any(ch not in string.hexdigits for ch in hcl):
        return False

    if fields["ecl"] not in eye_colors:
        return False

    if len(fields["pid"]) != 9 or any(d not in string.digits for d in fields["pid"]):
        return False

    return True


with open("input.txt") as f:
    data = (l.strip(string.whitespace) for l in f.readlines())


fields = {}
valid_passports = 0

for line in data:
    if line == "":
        if validate(fields):
            valid_passports += 1
        fields = {}
        continue

    elements = line.split()
    for element in elements:
        prefix, data = element.split(":")
        fields[prefix] = data

if validate(fields):
    valid_passports += 1

print(f"Valid passports: {valid_passports}")
