"""
ID: brkwok1
LANG: PYTHON3
TASK: ttwo
"""
import sys
sys.stderr.write('message')
from collections import deque
N = 10

fout = open('ttwo.out', 'w')
with open('ttwo.in', 'r') as fin:
    lines: str = fin.readlines()

    grid: list[list[str]] = [list(line.strip()) for line in lines]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'F':
                farmer = (i, j, 0)
            elif grid[i][j] == 'C':
                cows = (i, j, 0)

visited: set[tuple[tuple]] = set()
minutes: int = 0

def move(i, j, direction):
    if direction == 0:
        if i == 0 or grid[i-1][j] == '*':
            return (i, j, (direction + 1) % 4)
        else:
            return (i - 1, j, direction)
    elif direction == 1:
        if j == N - 1 or grid[i][j+1] == '*':
            return (i, j, (direction + 1) % 4)
        else:
            return (i, j + 1, direction)
    elif direction == 2:
        if i == N - 1 or grid[i+1][j] == '*':
            return (i, j, (direction + 1) % 4)
        else:
            return (i + 1, j, direction)
    elif direction == 3:
        if j == 0 or grid[i][j-1] == '*':
            return (i, j, (direction + 1) % 4)
        else:
            return (i, j - 1, direction)


while farmer[:2] != cows[:2] and (farmer, cows) not in visited:
    visited.add((farmer, cows))

    farmer = move(*farmer)
    cows = move(*cows)

    minutes += 1

if farmer[:2] == cows[:2]:
    fout.write(f"{minutes}\n")
else:
    fout.write("0\n")
    
fout.close()