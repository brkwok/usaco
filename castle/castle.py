"""
ID: brkwok1
LANG: PYTHON3
TASK: castle
"""
from collections import defaultdict
import sys
sys.stderr.write('message')

with open('castle.in', 'r') as fin:
    M, N = map(int, fin.readline().strip().split())
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    adj = defaultdict(set)

    rooms = [[-1] * M for i in range(N)]

    for i in range(N):
        line = list(map(int, fin.readline().strip().split()))
        for j, n in enumerate(line):
            b = bin(n + 16)[3:]
            curr_coord = (i, j)
            for k, ch in enumerate(b):
                if ch == "0":
                    dx, dy = dirs[k]
                    nei_coord = (i + dx, j + dy)
                    adj[curr_coord].add(nei_coord)
                    adj[nei_coord].add(curr_coord)

    def dfs(i, j, curr):
        if rooms[i][j] != -1:
            return 0

        rooms[i][j] = curr
        res = 1

        for x, y in adj[(i, j)]:
            res += dfs(x, y, curr)

        return res

    sizes = []
    curr = 0
    for i in range(N):
        for j in range(M):
            if rooms[i][j] == -1:
                sizes.append(dfs(i, j, curr))
                curr += 1

    max_combined_size = 0
    wall_to_remove = None
    
    for j in range(M):
        for i in reversed(range(N)):
            curr = rooms[i][j]
            for dx, dy in [(-1, 0), (0, 1)]:
                nei_x, nei_y = i + dx, j + dy

                if min(nei_x, nei_y) < 0 or \
                        nei_x >= N or \
                        nei_y >= M or \
                        curr == rooms[nei_x][nei_y]:
                    continue

                nei = rooms[nei_x][nei_y]

                max_size = sizes[curr] + sizes[nei]

                if max_size > max_combined_size:
                    max_combined_size = max_size
                    wall_to_remove = [i + 1, j + 1, "N" if dx == -1 else "E"]

    with open('castle.out', 'w') as fout:
        fout.write(str(len(sizes)) + '\n')
        fout.write(str(max(sizes)) + '\n')
        fout.write(str(max_combined_size) + '\n')
        fout.write(" ".join(map(str, wall_to_remove)) + "\n")
