"""
ID: brkwok1
LANG: PYTHON3
TASK: runround
"""
import sys
sys.stderr.write('message')

fin = open('runround.in', 'r')
fout = open('runround.out', 'w')

I = int(fin.readline().strip())
M = list(map(int, str(I)))
N = len(M)

def is_runround(arr):  
    runround = [False] * len(arr)

    x = 0
    for _ in range(len(arr)):
        runround[x] = True
        x = (x + arr[x]) % len(arr)

    return x == 0 and all(runround)

def next_runround(curr, used, md):
    if len(curr) == md:
        if int("".join(map(str, curr))) > I and is_runround(curr):
            return curr[:]
        
        return
    
    for i in range(1, 10):
        if used[i] == 0:
            used[i] = 1
            curr.append(i)
            res = next_runround(curr, used, md)
            curr.pop()
            used[i] = 0

            if res:
                return res
    

res = next_runround([], [0] * 10, N)
if not res:
    res = next_runround([], [0] * 10, N + 1)

fout.write(str(int("".join(map(str, res)))) + '\n')