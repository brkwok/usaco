"""
ID: brkwok1
LANG: PYTHON3
TASK: combo
"""
import sys
sys.stderr.write('message')


with open('combo.in', 'r') as fin:
    N = int(fin.readline().strip())
    f1, f2, f3 = map(int, fin.readline().strip().split())
    m1, m2, m3 = map(int, fin.readline().strip().split())

    def close(a, b):
        if abs(a - b) <= 2 or abs(a - b) >= N - 2:
            return True
        return False

    def close_enough(n1, n2, n3, k1, k2, k3):
        if close(n1, k1) and close(n2, k2) and close(n3, k3):
            return True
        
        return False

    res = 0
    for n1 in range(1, N + 1):
        for n2 in range(1, N + 1):
            for n3 in range(1, N + 1):
                if close_enough(n1, n2, n3, m1, m2, m3) or close_enough(n1, n2, n3, f1, f2, f3):
                    res += 1

    # avail_farmer = [ set() for i in range(3)]
    # avail_master = [ set() for i in range(3)]

    # for i in range(3):
    #     farmer_code = farmer[i]
    #     master_code = master[i]
    #     avail_farmer[i].add(farmer_code)
    #     avail_master[i].add(master_code)

    #     for j in range(2):
    #         farmer_code += 1
    #         if farmer_code > N:
    #             farmer_code = 1
    #         avail_farmer[i].add(farmer_code)

    #     for j in range(2):
    #         master_code += 1
    #         if master_code > N:
    #             master_code = 1
    #         avail_master[i].add(master_code)

    #     master_code = master[i]
    #     farmer_code = farmer[i]
    #     for j in range(2):
    #         farmer_code -= 1
    #         if farmer_code < 1:
    #             farmer_code = N
    #         avail_farmer[i].add(farmer_code)

    #     for j in range(2):
    #         master_code -= 1
    #         if master_code < 1:
    #             master_code = N
    #         avail_master[i].add(master_code)

    # intersection = [avail_farmer[i].intersection(avail_master[i]) for i in range(3)]

    # def calc_total_comb(set):
    #     comb = 1

    #     for s in set:
    #         comb *= len(s)

    #     return comb

    # res = calc_total_comb(avail_farmer) + calc_total_comb(avail_master) - calc_total_comb(intersection)

    with open('combo.out', 'w') as fout:
        fout.write(str(res) + '\n')
