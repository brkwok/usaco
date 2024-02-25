"""
ID: brkwok1
LANG: PYTHON3
TASK: skidesign
"""
import math
import heapq as hq
import sys
sys.stderr.write('message')


with open('skidesign.in', 'r') as fin:
    N = int(fin.readline().strip())
    
    hills = [0] * 101

    for i in range(N):
        height = int(fin.readline().strip())
        hills[height] += 1

    def cost(mn, mx, currMax):
        total = 0

        for i, h in enumerate(hills):
            if total > currMax:
                break
            if i < mn:
                total += h * (mn - i) ** 2
            elif i > mx:
                total += h * (i - mx) ** 2

        return total
    
    total = float('inf')
    for i in range(0, len(hills) - 17 + 1):
        mn, mx = i, i + 17

        c = cost(mn, mx, total)
        total = min(total, c)
        

    with open('skidesign.out', 'w') as fout:
        fout.write(str(total) + '\n')
        
