"""
ID: brkwok1
LANG: PYTHON3
TASK: subset
"""
from functools import lru_cache
fin = open('subset.in', 'r')
fout = open('subset.out', 'w')

N = int(fin.readline().strip())

total = (N * (N + 1)) // 2

if total % 2:
    fout.write('0\n')

else:
    dp = [[0] * (total + 1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        curr = i
        for j in range(total + 1):
            if j < curr:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - curr]

    count = dp[-1][total // 2]
    half = count / 2
    fout.write(f'{half}\n')

    # cache the input
    # @lru_cache(maxsize=None)
    # def dfs(curr_num, subset_sum):
    #     if subset_sum == 0:
    #         return 1

    #     if curr_num == 0 or subset_sum < 0:
    #         return 0

    #     res = 0
    #     res += dfs(curr_num - 1, subset_sum - curr_num) + \
    #         dfs(curr_num - 1, subset_sum)
        
    #     return res
    
    # count = dfs(N, total // 2)
    # output = count // 2
    # fout.write(f'{output}\n')
