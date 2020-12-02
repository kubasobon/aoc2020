import string


def count_valid_passwords(data):
    valid = 0
    for line in data:
        raw_policy, password = line.split(": ")
        raw_minmax, char = raw_policy.split()
        minimum, maximum = (int(i) for i in raw_minmax.split("-"))
        count = password.count(char)
        if minimum <= count <= maximum:
            valid += 1
    return valid


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [l for l in f.readlines() if l.strip(string.whitespace)]

    count = count_valid_passwords(data)
    print(f"valid passwords: {count}")
