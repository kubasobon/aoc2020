import string


# class Passport:
#     FIELDS = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")
#     def __init__(self):
#         self.byr = None   # (Birth Year)
#         self.iyr = None   # (Issue Year)
#         self.eyr = None   # (Expiration Year)
#         self.hgt = None   # (Height)
#         self.hcl = None   # (Hair Color)
#         self.ecl = None   # (Eye Color)
#         self.pid = None   # (Passport ID)
#         self.cid = None   # (Country ID)
#
#     def parse_line(self, line):
#         elements = line.split()
#         for element in elements:
#             prefix, data = element.split(":")
#             if prefix not in Passport.FIELDS:
#                 continue
#             setattr(self, prefix, data)


with open("input.txt") as f:
    data = (l.strip(string.whitespace) for l in f.readlines())

required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")  # , "cid")

fields = []
valid_passports = 0

for line in data:
    if line == "":
        if all(rf in fields for rf in required_fields):
            valid_passports += 1
        fields = []
        continue

    elements = line.split()
    for element in elements:
        prefix, data = element.split(":")
        fields.append(prefix)

if len(fields) > 0:
    if all(rf in fields for rf in required_fields):
        valid_passports += 1

print(f"Valid passports: {valid_passports}")
