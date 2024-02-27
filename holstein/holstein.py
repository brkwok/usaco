"""
ID: brkwok1
LANG: PYTHON3
TASK: holstein
"""
import sys
sys.stderr.write('message')

with open('holstein.in', 'r') as fin:
    V = int(fin.readline().strip())
    min_vitamins = list(map(int, fin.readline().strip().split()))
    G = int(fin.readline().strip())
    brands = []
    for i in range(G):
        nutrition = list(map(int, fin.readline().strip().split()))
        brands.append(nutrition)

    def sufficient(b):
        nutritions = [0] * V

        for i in range(G):
            if b & (1 << i):
                for idx, val in enumerate(brands[i]):
                    nutritions[idx] += val

        for have, need in zip(nutritions, min_vitamins):
            if have < need:
                return False
            
        return True
    
    mn = 1 << (G + 1)
    mn_len = G + 1
    for mask in range(1 << G):
        if sufficient(mask):
            l = bin(mask).count("1")

            if l < mn_len:
                mn = mask
                mn_len = l

    seq = []

    for i in range(G):
        if mn & (1 << i):
            seq.append(i + 1)
            

    # def suffice(vitamin):
    #     for i, v in enumerate(vitamin):
    #         if v < min_vitamins[i]:
    #             return False

    #     return True

    # mn = [1001, None]

    # def dfs(i, curr: list, curr_vitamin):
    #     if suffice(curr_vitamin):
    #         if len(curr) < mn[0]:
    #             mn[0] = len(curr)
    #             mn[1] = curr[:]
    #         return

    #     if i in used or len(curr) > mn[0]:
    #         return

    #     curr.append(i + 1)
    #     vitamin_info = brands[i]
    #     for j, v in enumerate(vitamin_info):
    #         curr_vitamin[j] += v

    #     used.add(i)

    #     for j in range(G):
    #         dfs(j, curr, curr_vitamin)

    #     used.remove(i)

    #     for j, v in enumerate(vitamin_info):
    #         curr_vitamin[j] -= v

    #     curr.pop()

    # for seq in range(G):
    #     dfs(seq, [], [0] * V)

    # res1, res2 = mn

    with open('holstein.out', 'w') as fout:
        fout.write(str(mn_len) + ' ' + " ".join(map(str, seq)) + '\n')
