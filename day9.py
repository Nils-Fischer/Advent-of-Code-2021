from math import prod
import re

with open("day9.txt", "r") as f:
    txt = [[int(y) for y in list(x)] for x in f.read().strip().split("\n")]
# --- Part One ---
risk = 0
for y in range(len(txt)):
    for x in range(len(txt[y])):
        if y != 0 and txt[y-1][x] <= txt[y][x]: continue
        if y != len(txt)-1 and txt[y+1][x] <= txt[y][x]: continue
        if x != 0 and txt[y][x-1] <= txt[y][x]: continue
        if x != len(txt[y])-1 and txt[y][x+1] <= txt[y][x]: continue
        risk += txt[y][x] + 1
print(risk)

# --- Part Two ---
def spread(basin):
    y, x = basin[-1]
    if y != 0 and (y-1, x) not in basin and txt[y-1][x] != 9: 
        basin.append((y-1,x)) 
        basin = spread(basin)
    if y != len(txt)-1 and (y+1, x) not in basin and txt[y+1][x] != 9:
        basin.append((y+1,x)) 
        basin = spread(basin)
    if x != 0 and (y, x-1) not in basin and txt[y][x-1] != 9: 
        basin.append((y, x-1))
        basin = spread(basin)
    if x != len(txt[0])-1 and (y, x+1) not in basin and txt[y][x+1] != 9: 
        basin.append((y, x+1))
        basin = spread(basin)
    return basin


basins = [] 
for y in range(len(txt)):
    for x in range(len(txt[y])):
        if y != 0 and txt[y-1][x] <= txt[y][x]: continue
        if y != len(txt)-1 and txt[y+1][x] <= txt[y][x]: continue
        if x != 0 and txt[y][x-1] <= txt[y][x]: continue
        if x != len(txt[y])-1 and txt[y][x+1] <= txt[y][x]: continue
        basins.append([(y, x)])

for i, basin in enumerate(basins):
    basins[i] = spread(basin) 
basins.sort(key=lambda x: len(x), reverse=True)
print(len(basins[0]) * len(basins[1]) * len(basins[2]))
