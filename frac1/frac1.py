"""
ID: brkwok1
LANG: PYTHON3
TASK: frac1
"""
from math import gcd
import sys
sys.stderr.write('message')

with open('frac1.in', 'r') as fin:
    N = int(fin.readline().strip())

    res = [(0, 1)]

    for i in range(1, N):
        for j in range(N, i, -1):
            curr_gcd = gcd(i, j)

            if curr_gcd == 1:
                res.append((i, j))

    res.append((1,1))

    res.sort(key=lambda x: x[0]/x[1])
    with open('frac1.out', 'w') as fout:
        for x,y in res:
            fout.write(f"{x}/{y}\n")
        
                
