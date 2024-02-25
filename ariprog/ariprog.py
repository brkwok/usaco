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

    bisquares = sorted(list(set(i ** 2 + j ** 2 for i in range(0, M + 1) for j in range(i, M + 1))))
    res = []

    def dfs(i, curr, diff):        
        if len(curr) >= N:
            res.append([curr[0], curr[1] - curr[0]])
            return
        
        if i >= len(bisquares):
            return
        
        if not curr or len(curr) == 1:
            curr.append(bisquares[i])
            dfs(i + 1, curr)
            curr.pop()
        else:
            diff = curr[1] - curr[0]
            diff2 = bisquares[i] - curr[-1]
            
            if diff == diff2:
                curr.append(bisquares[i])
                dfs(i + 1, curr)
                curr.pop()
        dfs(i + 1, curr, diff)

    # def solve(first, second, j):
    #     diff = second - first
    #     curr = second

    #     for k in range(j + 1, len(bisquares)):
    #         diff2 = bisquares[k] - curr
    #         # print(diff, diff2)
    #         if diff2 == diff:
    #             curr = bisquares[k]

    #             if (curr - first) // diff == N - 1:
    #                 res.append([first, diff])
    #                 return
    #         elif diff2 > diff:
    #             break


    # for i in range(len(bisquares)):
    #     for j in range(i + 1, len(bisquares)):
    #         solve(bisquares[i], bisquares[j], j)

    res.sort(key= lambda x: (x[1], x[0]))
    
    with open('ariprog.out', 'w') as fout:
        if res:
            for x,y in res:
                fout.write(f'{x} {y}\n')
        else:
            fout.write("NONE\n")

    