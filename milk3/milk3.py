"""
ID: brkwok1
LANG: PYTHON3
TASK: milk3
"""
from collections import deque
import sys
sys.stderr.write('message')


with open('milk3.in', 'r') as fin:
    cap = list(map(int, fin.readline().strip().split()))
    A, B, C = cap
    visited = [[False] * 21 for i in range(21)]

    res = set()

    def dfs(curr):
        A, B, C = curr
        if visited[B][C]:
            return

        if A == 0:
            res.add(C)

        visited[B][C] = True
        for i in range(3):
            for j in range(3):
                if i != j:
                    min_transferable = min(cap[j] - curr[j], curr[i])
                    curr[j] += min_transferable
                    curr[i] -= min_transferable
                    dfs(curr)
                    curr[j] -= min_transferable
                    curr[i] += min_transferable

    # cap = (A, B, C)
    # res = set([C])
    # seen = set()
    # q = deque([(0, 0, C)])

    # while q:
    #     buckets = q.popleft()

    #     seen.add(buckets)

    #     for i in range(3):
    #         for j in range(3):
    #             if i != j:
    #                 copy = list(buckets)
    #                 min_transferable = min(cap[j] - buckets[j], buckets[i])
    #                 copy[j] += min_transferable
    #                 copy[i] -= min_transferable
    #                 key = tuple(copy)

    #                 if key not in seen:
    #                     q.append(key)

    #                     if key[0] == 0:
    #                         res.add(key[2])

    dfs([0, 0, C])
    sorted_res = map(str, sorted(list(res)))

    with open('milk3.out', 'w') as fout:
        fout.write(" ".join(sorted_res)+"\n")
