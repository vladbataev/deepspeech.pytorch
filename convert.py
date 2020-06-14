def convert_to_tokens(number):
    tokens = []
    i = 0
    prev = None
    while number > 0:
        d = number % 10
        if i % 3 == 0 and i > 0:
            tokens.append(str(1000))
        if i % 3 == 2 and d > 0:
            tokens.append(str(100))
        if i % 3 == 1:
            if d == 1 or (tokens and tokens[-1] == "1000"):
                if tokens and tokens[-1] != "1000":
                    tokens.pop()
                if tokens and tokens[-1] == "1000" and d != 1:
                    if prev:
                        tokens.append(str(prev))
                    if d:
                        tokens.append(str(d * 10))
                else:
                    tokens.append(str(prev + d * 10))
            elif d:
                tokens.append(str(d * 10))
        else:
            if d:
                if not tokens or tokens[-1] not in ["100", "1000"]:
                    tokens.append(str(d))
                if d > 1 and tokens[-1] == "100":
                    tokens.append(str(d))
                if 2 <= number < 10 and tokens[-1] == "1000":
                    tokens.append(str(d))
        prev = d
        i += 1
        number = number // 10
    return tokens[::-1]


def tokens_to_number(tokens):
    mult = 1
    res = 0
    prev = None
    for d in tokens[::-1]:
        if d == "100":
            mult = mult * 100
        elif d == "1000":
            if prev == "100":
                res += 100
            mult = 1000
        else:
            res += mult * int(d)
        prev = d
    if prev in ["100", "1000"]:
        res += mult
    return res
