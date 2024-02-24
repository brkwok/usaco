"""
ID: brkwok1
LANG: PYTHON3
TASK: barn1
"""
import sys
sys.stderr.write('message')

with open('barn1.in', 'r') as fin:
    M, S, C = map(int, fin.readline().strip().split())

    stalls = [0] * S

    for i in range(C):
        stall_num = int(fin.readline().strip())
        stalls[stall_num-1] += 1

    trailing_zero_left = 0
    while stalls[trailing_zero_left] == 0:
        trailing_zero_left += 1

    trailing_zero_right = S - 1
    while stalls[trailing_zero_right] == 0:
        trailing_zero_right -= 1

    res = S - (S - 1 - trailing_zero_right) - (trailing_zero_left)

    consec_zeros = []

    prev = 1
    for i in range(trailing_zero_left, trailing_zero_right + 1):
        if stalls[i] == 0 and prev == 1:
            consec_zeros.append(-1)
        elif stalls[i] == 0 and prev == 0:
            consec_zeros[-1] -= 1

        prev = stalls[i]

    consec_zeros.sort()
    
    i = 0
    while i < len(consec_zeros) and i < M - 1:
        res += consec_zeros[i]
        i += 1

    with open('barn1.out', 'w') as fout:
        fout.write(str(res) + '\n')
        