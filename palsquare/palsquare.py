"""
ID: brkwok1
LANG: PYTHON3
TASK: palsquare
"""
import sys
sys.stderr.write('message')


def is_palindrome(s: str):
    return s == s[::-1]


def parse_num_to_base(base: int, num: int, code_map):
    res = []
    while num > 0:
        res.append(code_map[num % base])
        num //= base

    return "".join(res)[::-1]


with open('palsquare.in', 'r') as fin:
    base = int(fin.readline().strip())
    code_map = {i: ch for i, ch in enumerate("0123456789ABCDEFGHIJ")}

    res = []

    for i in range(1, 301):
        n1 = parse_num_to_base(base, i, code_map)
        n2 = parse_num_to_base(base, i**2, code_map)

        if is_palindrome(n2):
            res.append([n1, n2])

    with open('palsquare.out', 'w') as fout:
        for n1, n2 in res:
            fout.write(f'{n1} {n2}\n')




