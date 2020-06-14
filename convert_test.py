import random

from convert import convert_to_tokens, tokens_to_number


def test():
    for n in random.choices(range(1, int(1e+6)), k=100):
        tokens = convert_to_tokens(n)
        res = tokens_to_number(tokens)
        assert n == res, (n, tokens, res)
