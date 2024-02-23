"""
ID: brkwok01
LANG: PYTHON3
TASK: friday
"""
import sys
sys.stderr.write('message')

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

N = int(fin.readline().strip())
days = [0] * 7

startYear, endYear = 1900, 1900 + N


def is_leap_year(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True

    return False


# day of week, start monday
curr = [2]


def friday_thirteenth(year):
    days_in_month = {
        0: 31,
        1: 29 if is_leap_year(year) else 28,
        2: 31,
        3: 30,
        4: 31,
        5: 30,
        6: 31,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 31,
    }

    for d in days_in_month.values():
        thirteenth = (curr[0] + 12) % 7
        days[thirteenth] += 1
        curr[0] = (curr[0] + d) % 7


for i in range(startYear, endYear):
    friday_thirteenth(i)

output = " ".join(str(count) for count in days)
fout.write(output + "\n")
