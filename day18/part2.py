import string


def add(a, b):
    return a + b


def mul(a, b):
    return a * b

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
            level = token.count("(")
            for j in range(i + 1, len(equation_tokens)):
                subtoken = equation_tokens[j]
                if subtoken.startswith("("):
                    level += subtoken.count("(")
                elif subtoken.endswith(")"):
                    level -= subtoken.count(")")
                    if level == 0:
                        break
            else:
                raise Exception("No closing brace")
            # extract sub-equation tokens
            sub_equation = [token[1:]]
            sub_equation.extend(equation_tokens[i + 1 : j])
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


with open("input.txt") as f:
    data = [l.strip(string.whitespace) for l in f]

total = sum(execute(eq.split()) for eq in data)
print(f"Result: {total}")
