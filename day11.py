import itertools
import numpy as np

with open("day11.txt", "r") as f:
    txt = np.array([[int(y) for y in list(x)] for x in f.read().strip().split("\n")])

# --- Part One & Two---
count = 0
octos = txt

def flash(octos, x , y):
    dir = [x != 0, True, x != 9, y != 0, True, y != 9]
    for i, j in zip((0,1,1,1,0,-1,-1,-1),(-1,-1,0,1,1,1,0,-1)):
        if dir[1+i] and dir[4+j] and octos[x+i, y+j] != 10: 
            octos[x+i, y+j] += 1
            if octos[x+i, y+j] == 10: flash(octos, x+i, y+j)

for step in itertools.count():
    octos += 1
    x, y = np.where(txt==10)
    for i in range(len(x)):
        flash(octos, x[i], y[i])
    count += np.count_nonzero(octos==10)
    octos %= 10
    if step == 99: print(count)
    if np.all(octos == 0): 
        print(step+1)
        break


