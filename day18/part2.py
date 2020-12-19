import string


def execute(equation_tokens, lvl=0):
    assert isinstance(equation_tokens, list)
    no_braces = []
    i = 0
    while i < len(equation_tokens):
        token = equation_tokens[i]
        if token.startswith("("):
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
            no_braces.append(str(execute(sub_equation, lvl=lvl+1)))
            i = j
        else:
            no_braces.append(token)
        i += 1

    no_add = []
    i = 0
    active = False
    operands = []
    for token in no_braces:
        if token.isdigit() and active:
            operands.append(int(token))
        elif token.isdigit() and not active:
            no_add.append(token)
        elif token == "+" and active:
            pass # continue active
        elif token == "+" and not active:
            active = True
            operands.append(int(no_add[-1]))
            no_add = no_add[:-1]
        elif token == "*" and active:
            active = False
            no_add.append(str(sum(operands)))
            operands = []
            no_add.append(token)
        elif token == "*" and not active:
            no_add.append(token)
    if len(operands) > 0:
        no_add.append(str(sum(operands)))

    result = 1
    for token in no_add:
        if token.isdigit():
            result *= int(token)
        elif token == "*":
            pass
        else:
            raise Exception("Not what I expected")
    return result

with open("input.txt") as f:
    data = [l.strip(string.whitespace) for l in f]

total = sum(execute(eq.split()) for eq in data)
print(f"Result: {total}")

