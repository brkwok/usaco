"""
ID: brkwok1
LANG: PYTHON3
TASK: prefix
"""
import sys
sys.stderr.write('message')

fin = open('prefix.in', 'r')
fout = open('prefix.out', 'w')

from functools import lru_cache

primitives = []
primitives.reverse()

for line in fin:
    if line == '.\n':
        break
    primitives.extend(line.strip().split())

s: list[str] = []
for line in fin:
    s.append(line.strip())

S = ''.join(s)
N = len(S)


# @lru_cache(maxsize=None)
# def backtrack(i: int) -> int:
#     if i == N:
#         return 0
    
#     max_length = 0
#     for primitive in primitives:
#         if S.startswith(primitive, i):
#             max_length = max(max_length, len(primitive) + backtrack(i + len(primitive)))

#     return max_length

subsequence = [False] * (N + 1)
subsequence[0] = True
for i in range(N):
    if not subsequence[i]:
        continue
    for primitive in primitives:
        if S.startswith(primitive, i):
            subsequence[i + len(primitive)] = True

for i, val in enumerate(reversed(subsequence)):
    if val:
        fout.write(str(N - i) + '\n')
        break

fin.close()
fout.close()