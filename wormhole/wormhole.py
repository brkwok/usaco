"""
ID: brkwok1
LANG: PYTHON3
TASK: wormhole
"""
import sys
sys.stderr.write('message')

with open('wormhole.in', 'r') as fin:
    N = int(fin.readline().strip())
    X, Y = [0] * 13, [0] * 13
    pairs = [0] * 13
    next_on_right = [0] * 13

    for i in range(N):
        x, y = map(int, fin.readline().strip().split())
        X[i + 1], Y[i + 1] = x, y

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if X[j] > X[i] and Y[i] == Y[j]:
                if next_on_right[i] == 0 or ((X[j] - X[i]) < (X[next_on_right[i]] - X[i])):
                    next_on_right[i] = j

    def is_cycle():
        for start in range(1, N + 1):
            pos = start

            for j in range(N):
                pos = next_on_right[pairs[pos]]
            
            if pos != 0:
                return True
            
        return False

    def solve():
        total = 0

        for i in range(1, N + 2, 1):
            if i == N + 1 or pairs[i] == 0:
                break
        
        if i > N:
            if is_cycle():
                return 1
            else:
                return 0 
        
        for j in range(i + 1, N + 1):
            if pairs[j] == 0:
                pairs[i], pairs[j] = j, i
                total += solve()
                pairs[i] = pairs[j] = 0

        return total
    
    res = solve()
            
    with open('wormhole.out', 'w') as fout:
        fout.write(str(res) + '\n')

        