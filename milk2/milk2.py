"""
ID: brkwok1
LANG: PYTHON3
TASK: milk2
"""
import sys
sys.stderr.write('message')

def mergeIntervals(intervals):
    new_intervals = [intervals[0]]

    for i in range(1, len(intervals)):
        start, end = intervals[i]

        if start <= new_intervals[-1][1]:
            new_intervals[-1][1] = max(new_intervals[-1][1], end)
        else:
            new_intervals.append(intervals[i])

    return new_intervals


with open('milk2.in', 'r') as fin:
    N = int(fin.readline())
    intervals = []

    for i in range(N):
        start, end = map(int, fin.readline().strip().split())
        intervals.append([start, end])
    
    intervals.sort()

    intervals = mergeIntervals(intervals)

    max_time = 0
    
    for start, end in intervals:
        max_time = max(max_time, end - start)

    no_milk = 0

    for i in range(1, len(intervals)):
        prev_end = intervals[i - 1][1]
        curr_start = intervals[i][0]

        no_milk = max(no_milk, curr_start - prev_end)

    with open('milk2.out', 'w') as fout:
        fout.write(f"{max_time} {no_milk}\n")