import string


def count_valid_passwords(data):
    valid = 0
    for line in data:
        raw_policy, password = line.split(": ")
        raw_ab, char = raw_policy.split()
        a, b = (int(i) for i in raw_ab.split("-"))
        assert a <= len(password) and b <= len(password)
        if (password[a-1] == char) ^ (password[b-1] == char):
            valid += 1
    return valid


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [l for l in f.readlines() if l.strip(string.whitespace)]

    count = count_valid_passwords(data)
    print(f"valid passwords: {count}")
