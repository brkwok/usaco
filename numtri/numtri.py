"""
ID: brkwok1
LANG: PYTHON3
TASK: numtri
"""
import sys
sys.stderr.write('message')

with open('numtri.in', 'r') as fin:
    N = int(fin.readline().strip())
    rows = [list(map(int, line.strip().split())) for line in fin.readlines()]

    best = [0] * N
    for row in rows:
        for i in range(len(row) - 1, 0, -1):
            best[i] = max(best[i - 1], best[i]) + row[i]

        best[0] += row[0]
            

    with open('numtri.out', 'w') as fout:
        fout.write(str(max(best)) + '\n')