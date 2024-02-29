"""
ID: brkwok1
LANG: PYTHON3
TASK: preface
"""
import sys
sys.stderr.write('message')

fin = open('preface.in', 'r')
fout = open('preface.out', 'w')

N = int(fin.readline().strip())

roman = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
         (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

ch_count = {ch: 0 for i, ch in enumerate("IVXLCDM")}

def to_roman(n):
    res = []

    for num, ch in roman:
        if num <= n:
            while n > 0 and num <= n:
                res.append(ch)
                n -= num

    return "".join(res)

for i in range(1, N + 1):
    for ch in to_roman(i):
        ch_count[ch] += 1

for ch, count in ch_count.items():
    if count:
        fout.write(f'{ch} {count}\n')