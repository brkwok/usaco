"""
ID: brkwok1
LANG: PYTHON3
TASK: milk
"""
import sys
sys.stderr.write('message')

with open('milk.in', 'r') as fin:
    need, num_vendors = map(int, fin.readline().strip().split())

    vendor_prices = []
    for i in range(num_vendors):
        price, num_units = map(int, fin.readline().strip().split())
        vendor_prices.append([price, num_units])

    vendor_prices.sort()

    res = 0
    i = 0
    while need > 0 and i < len(vendor_prices):
        p, u = vendor_prices[i]

        res += p * min(need, u)
        need -= min(need, u)

        i += 1

    with open('milk.out', 'w') as fout:
        fout.write(str(res) + "\n")

        