"""
ID: brkwok1
LANG: PYTHON3
TASK: ariprog
"""
import sys
sys.stderr.write('message')
from collections import defaultdict, deque

with open('ariprog.in', 'r') as fin:
    N = int(fin.readline().strip())
    M = int(fin.readline().strip())

    bisquares = set()
    for i in range(M + 1):
        for j in range(i, M + 1):
            bisquares.add(i*i + j*j)
    
    list_bs = sorted(list(bisquares))
    L = len(list_bs)
    res = []

    for i in range(L - 1, N - 2, -1):
        end = list_bs[i]
        diff = 1
        max_step = end // (N - 1)
        next_seq = list_bs[i - diff]
        curr_step = end - next_seq

        while curr_step <= max_step:
            is_inset = True

            for n in range(N - 2):
                next_seq -= curr_step

                if next_seq not in bisquares:
                    is_inset = False
                    break
                
            if is_inset:
                res.append((end - curr_step * (N - 1), curr_step))

            diff += 1
            next_seq = list_bs[i - diff]
            curr_step = end - next_seq

    res.sort(key= lambda x: (x[1], x[0]))

    with open('ariprog.out', 'w') as fout:
        if res:
            for x,y in res:
                fout.write(f'{x} {y}\n')
        else:
            fout.write('NONE\n')