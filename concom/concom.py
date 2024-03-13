"""
ID: brkwok1
LANG: PYTHON3
TASK: concom
"""
import sys
sys.stderr.write('message')
from collections import defaultdict


with open('concom.in', 'r') as fin:
    N = int(fin.readline())
    
    controls = defaultdict(dict)
    for _ in range(N):
        parent, child, percent = map(int, fin.readline().strip().split())
        controls[parent][child] = percent

    visited = set()
    def dfs(node: int, c: list):
        if node in visited:
            return
        
        visited.add(node)

        for child in controls[node]:
            c[child] += controls[node][child]
            if c[child] > 50:
                dfs(child, c)

        visited.remove(node)

    res = []
    for n in list(controls.keys()):
        c = [0] * 101
        dfs(n, c)

        for i, v in enumerate(c):
            if v > 50 and i != n:
                res.append((n, i))

    res.sort(key=lambda x: (x[0], x[1]))

    with open('concom.out', 'w') as fout:
        for r in res:
            fout.write(f'{r[0]} {r[1]}\n')
    