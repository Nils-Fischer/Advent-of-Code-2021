import re
from typing import SupportsIndex

with open("day8.txt", "r") as f:
    txt = [[set(y) for y in x[0].strip().split(" ")] for x in re.findall(r"([a-z ]+)|([a-z ]+)",f.read())]

# --- Part One ---
count = 0
for i in range(1, len(txt), 2):
    txt[i-1] = sorted(txt[i-1], key=lambda x: len(x))
    for x in txt[i]:
        if len(x) in [2,3,4,7]: count += 1
print(count)

# --- Part Two ---
seg = []
for i in range(0, len(txt), 2):
    num = [0, txt[i][0], 0, 0, txt[i][2], 0, 0, txt[i][1], txt[i][-1], 0,]
    for x in txt[i][3:6]:
        if x >= num[1]: num[3] = x
        elif len(x.intersection(num[4])) == 3: num[5] = x
        else: num[2] = x
    for x in txt[i][6:9]:
        if x >= num[4]: num[9] = x
        elif x >= num[5]: num[6] = x
        else: num[0] = x
    dig = ""
    for j in range(4):
        dig += str(num.index(txt[i+1][j]))
    seg.append(int(dig))
print(sum(seg))
