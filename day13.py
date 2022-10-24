import re
import numpy as np

with open("day13.txt", "r") as f:
    txt = f.read().strip()

instructions = np.array(re.findall(r"([xy])=(\d+)", txt))
points = np.array(re.findall(r"(\d+),(\d+)", txt))
max_x = int(max(points, key=lambda x: int(x[0]))[0])
max_y = int(max(points, key=lambda x: int(x[1]))[1])


# --- Part One ---
cut = int(instructions[0][1])
fold = np.zeros((max_y+1, cut))
for x, y in map(lambda x: (int(x[0]),int(x[1])), points): 
    if x >= cut: x = 2*cut - x
    fold[y, x] = 1

print(np.count_nonzero(fold==1))

# --- Part Two ---
def fold(sheet, x, y):
    new = np.zeros((y,x))
    points = np.where(sheet==1)
    for j, i in zip(points[0], points[1]):
        if i > x * 2 or j > y * 2: continue
        if j > y: j = 2*y - j 
        if i > x: i = 2*x - i
        new[j, i] = 1
    return new

sheet = np.zeros((max_y+1, max_x+1))
for x, y in map(lambda x: (int(x[0]),int(x[1])), points): 
    sheet[y, x] = 1

for instruction in instructions:
    x = int(instruction[1]) if instruction[0] == "x" else len(sheet[0])
    y = int(instruction[1]) if instruction[0] == "y" else len(sheet)
    sheet = fold(sheet, x, y)
    
print(sheet)
    