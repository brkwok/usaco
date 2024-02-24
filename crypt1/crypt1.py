"""
ID: brkwok1
LANG: PYTHON3
TASK: crypt1
"""
import sys
sys.stderr.write('message')

# with open('crypt1.in', 'r') as fin:
#     N = int(fin.readline().strip())
#     digs = fin.readline().strip().split()
#     s = set(digs)

#     poss_digits = []
#     three_digs = []
#     two_digs = []

#     def create_num(max_len, poss_digits, res_arr):
#         if len(poss_digits) >= max_len:
#             res_arr.append("".join(poss_digits))
#             return

#         for i in range(len(digs)):
#             poss_digits.append(digs[i])
#             create_num(max_len, poss_digits, res_arr)
#             poss_digits.pop()

#         return

#     create_num(3, poss_digits, three_digs)
#     create_num(2, poss_digits, two_digs)

#     def check_in_set(num, s, l):
#         n = str(num)

#         if len(n) != l:
#             return False

#         for ch in n:
#             if ch not in s:
#                 return False

#         return True

#     def is_crypt(s1, s2):
#         n1,n2 = int(s1), int(s2)
#         p1 = n1 * (n2 % 10)
#         p2 = n1 * (n2 // 10)

#         if check_in_set(p1,s,3) and check_in_set(p2, s,3) and check_in_set(n1 * n2, s,4):
#             return True
#         return False

#     res = 0
#     for i in range(len(three_digs)):
#         for j in range(len(two_digs)):
#             if is_crypt(three_digs[i], two_digs[j]):
#                 res += 1

#     with open('crypt1.out', 'w') as fout:
#         fout.write(str(res) + '\n')

with open('crypt1.in', 'r') as fin:
    N = int(fin.readline().strip())
    nums = set(map(int, fin.readline().strip().split()))

    def is_good(n, l):
        if len(str(n)) != l:
            return False

        while n > 0:
            dig = n % 10
            if dig not in nums:
                return False
            n = n // 10

        return True

    def is_good_prod(i, j):
        if not is_good(i, 3) or not is_good(j, 2) or not is_good(i * j, 4):
            return False
        
        while j:
            if not is_good(i * (j % 10), 3):
                return False
            j = j // 10

        return True

    res = 0
    for i in range(100, 1000):
        for j in range(10, 100):
            if is_good_prod(i, j):
                res += 1

    with open('crypt1.out', 'w') as fout:
        fout.write(str(res) + '\n')
