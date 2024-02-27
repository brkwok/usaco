"""
ID: brkwok1
LANG: PYTHON3
TASK: sort3
"""
import sys
sys.stderr.write('message')

with open('sort3.in', 'r') as fin:
    N = int(fin.readline().strip())

    counts = [0] * 4
    nums = []

    for i in range(N):
        num = int(fin.readline().strip())
        counts[num] += 1
        nums.append(num)


    correct_order = [i for i, count in enumerate(counts) for j in range(count)]
    
    misplaced = [[0] * 4 for i in range(4)]

    for i, z in enumerate(zip(nums, correct_order)):
        n1, n2 = z
        if n1 != n2:
            misplaced[n2][n1] += 1

    res = 0

    for i in range(1, 4):
        for j in range(1, 4):
            if i != j:
                first = misplaced[i]
                second = misplaced[j]
                mn = min(first[j], second[i])
                res += mn
                first[j] -= mn
                second[i] -= mn

    leftover = sum(n for row in misplaced for n in row)
    res += 2 * (leftover // 3)

    # first = misplaced[1]
    # print(misplaced)

    # for i in range(2, 4):
    #     other = misplaced[i]
    #     mn = min(first[i], other[1])
    #     res += mn
    #     first[i] -= mn
    #     other[1] -= mn

    # print(misplaced, res)

        
    # r = N - 1
    # three_threshold = l = N - count[3] - 1

    # res = 0
    # while r > three_threshold:
    #     while r > three_threshold and nums[r] == 3:
    #         r -= 1
        
    #     while l >= 0 and nums[l] != 3:
    #         l -= 1

    #     if r > three_threshold:
    #        res += 1
    #        nums[r], nums[l] = nums[l], nums[r]

    # displaced = 0
    # for i in range(count[1]):
    #     if nums[i] != 1:
    #         displaced += 1

    with open('sort3.out', 'w') as fout:
        fout.write(str(res) + '\n')