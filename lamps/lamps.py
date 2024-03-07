"""
ID: brkwok1
LANG: PYTHON3
TASK: lamps
"""
import sys
sys.stderr.write('message')

fin = open('lamps.in', 'r')
fout = open('lamps.out', 'w')

N = int(fin.readline().strip())
C = int(fin.readline().strip())

initial = [True] * N

on = list(map(int, fin.readline().split()))
off = list(map(int, fin.readline().split()))

def click_button(button, lamps):
    if button == 1:
        return [not x for x in lamps]
    elif button == 2:
        return [not x if i%2 ==0 else x for i, x in enumerate(lamps)]
    elif button == 3:
        return [not x if i % 2 == 1 else x for i,x in enumerate(lamps)]
    else:
        return [not x if i % 3 == 0 else x for i,x in enumerate(lamps)]
    
def is_on(lamps):
    for i in on:
        if i != -1:
            if not lamps[i - 1]:
                return False
            
    return True

def is_off(lamps):
    for i in off:
        if i != -1:
            if lamps[i - 1]:
                return False
            
    return True

poss = [[] for _ in range(5)]
from itertools import combinations

for r in range(5):
    for comb in combinations(range(1,5), r):
        lamps = initial[:]
        for c in comb:
            lamps = click_button(c, lamps)
        poss[r].append(lamps)


res = []
for r in range(5):
    if r <= C and (C - r) % 2 == 0:
        for lamps in poss[r]:
            if is_on(lamps) and is_off(lamps):
                res.append("".join("1" if x else "0" for x in lamps))

res = set(res)

if not res:
    fout.write("IMPOSSIBLE\n")
else:
    for s in sorted(res):
        fout.write(s + "\n")

fin.close()
fout.close()

