"""
ID: brkwok1
LANG: PYTHON3
TASK: beads
"""
import sys
sys.stderr.write('message')

with open('beads.in', 'r') as fin:
    N = int(fin.readline().strip())
    beads = fin.readline().strip()

    circle = beads + beads
    m = 0
    l = 0
    res = 0

    for i in range(1, len(circle)):
        l = i - 1
        r = i
        curr_left = circle[i - 1]
        curr_right = circle[i]

        while (r - l + 1) < N and l - 1 >= 0 and circle[l] == "w":
            l -= 1

        curr_left = circle[l]

        while (r - l + 1) < N and l - 1 >= 0 and (circle[l - 1] == "w" or circle[l - 1] == curr_left):
            l -= 1

        while (r - l + 1) < N and r + 1 < len(circle) and circle[r] == "w":
            r += 1

        curr_right = circle[r]

        while (r - l + 1) < N and r + 1 < len(circle) and (circle[r + 1] == "w" or circle[r + 1] == curr_right):
            r += 1

        res = max(res, r - l + 1)

    with open('beads.out', 'w') as fout:
        fout.write(str(res) + "\n")
