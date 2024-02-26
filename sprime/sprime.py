"""
ID: brkwok1
LANG: PYTHON3
TASK: sprime
"""
import math
import sys
sys.stderr.write('message')

with open('sprime.in', 'r') as fin:
    with open('sprime.out', 'w') as fout:
        N = int(fin.readline().strip())

        def is_prime(n):
            if n == 2:
                return True
            
            if n % 2 == 0:
                return False
            
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
                
            return True
        
        def gen_num(n, curr_num_digit, max_num_digit):
            if curr_num_digit == max_num_digit:
                if is_prime(n):
                    fout.write(str(n) + '\n')
                else:
                    return

            for i in range(1, 10, 2):
                next_num = n * 10 + i
                if is_prime(next_num):
                    gen_num(next_num, curr_num_digit + 1, max_num_digit)

        for i in [2,3,5,7]:
            gen_num(i, 1, N)
