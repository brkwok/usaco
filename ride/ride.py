"""
ID: brkwok1
LANG: PYTHON3
TASK: ride
"""
import sys
sys.stderr.write('message')

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')


def calcMod(com: str):
    num_map = {ch: i + 1 for i, ch in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

    res = 1
    for ch in com:
        res *= num_map[ch]

    return res % 47


comet = calcMod(fin.readline().strip())
group = calcMod(fin.readline().strip())

output = "GO" if comet == group else "STAY"

fout.write(output + '\n')
fout.close
