"""
ID: brkwok1
LANG: PYTHON3
TASK: maze1
"""
from collections import deque
import sys
sys.stderr.write('message')


with open('maze1.in', 'r') as fin:
    W, H = map(int, fin.readline().split())
    maze = [fin.readline()[:2 * W + 1] for _ in range(2*H+1)]



exits = []

for i in range(1, 2*H+1, 2):
    if maze[i][0] == ' ':
        exits.append((i, 1))
    if maze[i][-1] == ' ':
        exits.append((i, (2 * W - 1)))

for i in range(1, 2 * W + 1, 2):
    if maze[0][i] == ' ':
        exits.append((1, i))
    if maze[-1][i] == ' ':
        exits.append(((2 * H - 1), i))


nei = [(0, 2), (0, -2), (2, 0), (-2, 0)]

def bfs(exits):
    visited: set[tuple] = set()
    q = deque([(e, 1) for e in exits])
    while q:
        (x, y), d = q.popleft()
        visited.add((x, y))

        for dx, dy in nei:
            nx, ny = x + dx, y + dy

            if 0 < nx < 2 * H and 0 < ny < 2 * W and (nx, ny) not in visited and maze[x + dx // 2][y + dy // 2] == ' ':
                visited.add((nx,ny))
                q.append(((nx, ny), d + 1))

    return d

r = bfs(exits)

with open('maze1.out', 'w') as fout:
    fout.write(str(r) + '\n')