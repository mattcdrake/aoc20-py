def p1(input_path: str) -> str:
    with open(input_path) as f:
        vals = [int(line) for line in f.readlines()]

    for ind1, val1 in enumerate(vals):
        for val2 in vals[ind1+1:]:
            if val1 + val2 == 2020:
                return str(val1 * val2)

    return "Couldn't solve this one"


def p2(input_path: str) -> str:
    with open(input_path) as f:
        vals = [int(line) for line in f.readlines()]

    for ind1, val1 in enumerate(vals):
        for ind2, val2 in enumerate(vals[ind1+1:]):
            for val3 in vals[ind2+1:]:
                if val1 + val2 + val3 == 2020:
                    return str(val1 * val2 * val3)

    return "Couldn't solve this one"

