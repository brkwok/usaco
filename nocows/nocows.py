"""
ID: brkwok1
LANG: PYTHON3
TASK: nocows
"""
from functools import lru_cache
import sys
sys.stderr.write('message')

fin = open('nocows.in', 'r')
fout = open('nocows.out', 'w')
N, K = map(int, fin.readline().strip().split())

MOD = 9901
trees = [[0] * (N + 1) for _ in range(K + 1)]
trees[1][1] = 1

for k in range(2, K+1):
    for n in range(1, N+1):
        trees[k][n] = trees[k-1][n]


        for i in range(1, n//2):
            trees[k][n] += 2 * trees[k-1][i] * trees[k-1][n-i-1]
            trees[k][n] -= 2 * trees[k-2][i] * trees[k-2][n-i-1]

        if n % 2 == 1:
            i = n // 2
            trees[k][n] += trees[k-1][i] * trees[k-1][n-i-1]
            trees[k][n] -= trees[k-2][i] * trees[k-2][n-i-1]

        trees[k][n] %= 9901

fout.write(str((trees[K][N] - trees[K-1][N] + MOD) % MOD) + '\n')

fin.close()
fout.close()
