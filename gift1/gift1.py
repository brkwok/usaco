"""
ID: brkwok01
LANG: PYTHON3
TASK: gift1
"""
import sys

sys.stderr.write('message')

# input given
with open('gift1.in', 'r') as fin:
    N = int(fin.readline().strip())
    names = []
    money = [0] * N

    for i in range(N):
        names.append(fin.readline().strip())

    name_map = { name: i for i, name in enumerate(names)}

    for i in range(N):
        name = fin.readline().strip()
        withdrawal, num_people = map(int, fin.readline().strip().split())
        
        if num_people == 0:
            continue
        
        money[name_map[name]] -= withdrawal
        each_money = withdrawal // num_people
        for i in range(num_people):
            person_to_receive = fin.readline().strip()
            money[name_map[person_to_receive]] += each_money

        money[name_map[name]] += withdrawal % num_people

    with open('gift1.out', 'w') as fout:
        
        for name, money in zip(names, money):
            fout.write(f"{name} {money}\n")


