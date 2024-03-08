"""
ID: brkwok1
LANG: PYTHON3
TASK: money
"""
import sys
sys.stderr.write('message')

with open('money.in', 'r') as fin:
    V, N = map(int, fin.readline().strip().split())
    coins = set()
    
    for line in fin:
        coins.update(map(int, line.strip().split()))

coins = sorted(list(coins))

dp = [0] * (N + 1)
dp[0] = 1
for coin in coins:
    for i in range(coin, N + 1):
        dp[i] += dp[i - coin]

with open('money.out', 'w') as fout:
    fout.write(str(dp[N]) + '\n')