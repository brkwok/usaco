"""
ID: brkwok1
LANG: PYTHON3
TASK: pprime
"""
import math
import sys
sys.stderr.write('message')


with open('pprime.in', 'r') as fin:
    with open('pprime.out', 'w') as fout:
        A, B = map(int, fin.readline().strip().split())
        A = A if A % 2 else A + 1

        def is_prime(n):
            if n < 2:
                return False

            if n % 2 == 0:
                return n == 2

            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False

            return True

        min_base = math.floor(math.log10(A))
        max_base = math.ceil(math.log10(B))
        print(min_base, max_base)

        for exp in range(min_base, max_base):
            for n in range(10**(exp // 2), 10**(exp // 2 + 1)):
                palin = str(n)

                if exp % 2:
                    palin = palin + palin[::-1]
                else:
                    palin = palin + palin[:-1][::-1]

                prime = int(palin)

                if A <= prime <= B and is_prime(prime):
                    fout.write(palin + '\n')