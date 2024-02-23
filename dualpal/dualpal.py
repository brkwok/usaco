"""
ID: brkwok1
LANG: PYTHON3
TASK: dualpal
"""
import sys
sys.stderr.write('message')

def parse_num_to_base(base: int, num: int):
    res = []
    while num > 0:
        res.append(str(num % base))
        num //= base

    return "".join(res)[::-1]

def is_palin(s):
    return s == s[::-1]

def check_dual(n):
    count = 0
    for i in range(2, 11):
        if is_palin(parse_num_to_base(i, n)):
            count += 1
    
    if count > 1:
        return True
    
    return False

fout = open('dualpal.out', 'w')

with open('dualpal.in', 'r') as fin:
    N, S = map(int, fin.readline().strip().split())
    res = []

    S += 1
    while len(res) < N:
        if check_dual(S):
            res.append(S)
        S += 1
    
    for n in res:
        fout.write(str(n) + "\n")

fout.close()
