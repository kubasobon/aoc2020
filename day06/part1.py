import string

with open("input.txt") as f:
    data = (l.strip(string.whitespace) for l in f.readlines())

total_yes = 0
group_answers = set()

for l in data:
    if l == "":
        total_yes += len(group_answers)
        group_answers = set()
        continue
    group_answers.update(l)

if len(group_answers) > 0:
    total_yes += len(group_answers)

print(f"Total questions answered 'yes': {total_yes}")
