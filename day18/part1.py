import string

def splitd(s, sep, maxsplit=-1):
    """splitd splits the string but keeps delimiters"""
    out = []
    for token in s.split(sep, maxsplit):
        out.append(token)
        out.append(sep)
    return out[:-1]


def add(a, b):
    return a + b

def mul(a, b):
    return a * b


data = "3 * 4 * 2 * 5 * (3 + 4 * (6 + 3 + 2 + 8 + 4) + 5 * 7)"

def execute(equation_tokens):
    acc = None
    operator = None

    i = 0
    while i < len(equation_tokens):
        token = equation_tokens[i]

        if token == "+":
            operator = add
            i += 1
            continue
        elif token == "*":
            operator = mul
            i += 1
            continue
        elif token.startswith("("):
            # find closing brace
            level = 0
            for j in range(i+1, len(equation_tokens)):
                if equation_tokens[j].startswith("("):
                    level += 1
                elif equation_tokens[j].endswith(")"):
                    if level > 0:
                        level -= 1
                    else:
                        break
            else:
                raise Exception("No closing brace")
            # extract sub-equation tokens
            sub_equation = [token[1:]]
            sub_equation.extend(equation_tokens[i+1:j])
            sub_equation.append(equation_tokens[j][:-1])
            token = str(execute(sub_equation))
            i = j

        assert token.isdigit()

        if acc is None:
            acc = int(token)
        elif acc and operator:
            acc = operator(acc, int(token))
            operator = None
        else:
            raise Exception("Two consecutive tokens")
        i += 1

    assert operator is None
    return acc

print(execute(data.split()))

