"""
ID: brkwok1
LANG: PYTHON3
TASK: hamming
"""
import sys
sys.stderr.write('message')

fin = open('hamming.in', 'r')
fout = open('hamming.out', 'w')

# Num res, Num bits, Distance
N, B, D = map(int, fin.readline().strip().split())

res = [0]
seen = set()

for n in range(1 << B):
    if len(res) == N:
        break

    for num in res:
        if bin(n ^ num)[2:].count("1") < D:
            break
    else:
        res.append(n)

for i in range(N // 10 + 1):
    part = res[i * 10: (i * 10 + 10)]
    if part:
        fout.write(" ".join(map(str, part)) + '\n')



