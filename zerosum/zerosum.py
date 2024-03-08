"""
ID: brkwok1
LANG: PYTHON3
TASK: zerosum
"""
import sys
sys.stderr.write('message')

with open('zerosum.in', 'r') as fin:
    N = int(fin.readline().strip())

s = "".join(map(str,range(1, N + 1)))

res = []

def dfs(i, curr_path):
    if i == N:
        if eval(curr_path.replace(' ', '')) == 0:
            res.append(curr_path)
        return
    
    dfs(i + 1, curr_path + ' ' + s[i])
    dfs(i + 1, curr_path + '+' + s[i])
    dfs(i + 1, curr_path + '-' + s[i])


dfs(1, '1')
with open('zerosum.out', 'w') as fout:
    for r in res:
        print(r, file=fout)
