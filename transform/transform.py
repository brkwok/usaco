"""
ID: brkwok1
LANG: PYTHON3
TASK: transform
"""
import sys
sys.stderr.write('message')

def rotate(arr):
    # transpose and reverse each row to rotate 90 deg
    N = len(arr)

    for i in range(N):
        for j in range(i + 1, N):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(N):
        arr[i] = arr[i][::-1]

    return arr

def check_same(original, output):
    N = len(original)

    for i in range(N):
        for j in range(N):
            if original[i][j] != output[i][j]:
                return False
            
    return True

def check_reflection(original, output):
    N = len(original)
    
    for i in range(N):
        for j in range(N):
            if original[i][j] != output[i][N - j - 1]:
                return False
            
    return True

def check_change(original, output):
    changes = [False] * 6

    if check_same(original, output):
        changes[5] = True
    
    if check_reflection(original, output):
        changes[3] = True
    
    for i in range(3):        
        original = rotate(original)
        
        if check_same(original,output):
            changes[i] = True
        
        if check_reflection(original, output):
            changes[4] = True

    return changes
    

with open('transform.in', 'r') as fin:
    N = int(fin.readline().strip())
    original = [list(fin.readline().strip()) for i in range(N)]
    output = [list(fin.readline().strip()) for i in range(N)]

    changes = check_change(original, output)
    
    res = 0

    for i, c in enumerate(changes):
        if c:
            res = i + 1
            break
    
    if res == 0:
        res = 7

    with open('transform.out', 'w') as fout:
        fout.write(str(res) + "\n")