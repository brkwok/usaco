"""
ID: brkwok1
LANG: PYTHON3
TASK: namenum
"""
import sys
sys.stderr.write('message')

fout = open('namenum.out', 'w')

def parse_code_to_name(s, c_map, n):
    for i, ch in enumerate(s):
        if ch.upper() not in c_map or c_map[ch.upper()] != n[i]:
            return False
        
    return True
with open('namenum.in','r') as fin:
    cow_num = fin.readline().strip()
    chars = "ABCDEFGHIJKLMNOPRSTUVWXY"
    char_map = {ch: str(i // 3 + 2) for i, ch in enumerate(chars)}

    if '1' in cow_num:
        fout.write('NONE')
        fout.close()
    else:
        res = []
        with open('dict.txt', 'r') as data:
            for line in data:
                name = line.strip()
                if len(name) == len(cow_num):
                    if parse_code_to_name(name, char_map, cow_num):
                        res.append(name.upper())


        if res:
            fout.write("\n".join(res) + "\n")
        else:
            fout.write('NONE\n')

        fout.close()




        