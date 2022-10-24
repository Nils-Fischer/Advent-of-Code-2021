# --- Day 3: Binary Diagnostic ---
import numpy as np
from collections import Counter
with open("day3.txt", "r") as f:
    txt = [list(x) for x in f.read().strip().split("\n")]
# --- Part one --- 

gamma = delta = ""
rot = np.rot90(txt, 3)
for s in rot:
    gamma += Counter(s).most_common(1)[0][0]
    delta += Counter(s).most_common(2)[1][0]
gamma = int(gamma, 2)
delta = int(delta, 2)
print(gamma*delta)

#--- Part Two ---
oxy = txt
for i in range(len(txt[0])): 
    rot = np.rot90(oxy, 3)
    oxy = [x for x in oxy if x[i] == Counter(sorted(rot[i],reverse=True)).most_common()[0][0]]
oxy = int("".join(oxy[0]), 2)
co2 = txt
for i in range(len(txt[0])-1): 
    if len(co2) == 1: break
    rot = np.rot90(co2, 3)
    co2 = [x for x in co2 if x[i] == Counter(sorted(rot[i],reverse=True)).most_common()[1][0]] 
co2 = int("".join(co2[0]), 2)
print(oxy * co2)