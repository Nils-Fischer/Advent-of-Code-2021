import re
import numpy as np

with open("day5.txt", "r") as f:
    txt = [x.split(",") for x in re.sub(r"(\d+),(\d+) -> (\d+),(\d+)\n?", lambda x: f"{x.group(1)},{x.group(2)},{x.group(3)},{x.group(4)}.",f.read().strip()).split(".")][:-1]

# --- Part one ---
vert = [[int(i) for i in x] for x in txt if x[0] == x[2] or x[1] == x[3]]
floor = np.zeros((1000,1000))

def vents(floor, line):
    x = abs(line[2] - line[0]) // (line[2] - line[0]) if line[2] - line[0] != 0 else 0
    y = abs(line[3] - line[1]) // (line[3] - line[1]) if line[3] - line[1] != 0 else 0
    i = 0
    while(True):
        floor[(line[1] + y * i), (line[0] + x * i)] += 1
        if (line[0] + x * i, line[1] + y * i) == (line[2], line[3]): break
        i += 1
    pass
for line in vert:
    vents(floor, line)
print(sum([1 for x in floor.flatten() if x > 1.0]))

# --- Part Two ---
lines = [[int(i) for i in x] for x in txt]
floor = np.zeros((1000,1000))

def vents(floor, line):
    x = abs(line[2] - line[0]) // (line[2] - line[0]) if line[2] - line[0] != 0 else 0
    y = abs(line[3] - line[1]) // (line[3] - line[1]) if line[3] - line[1] != 0 else 0
    i = 0
    while(True):
        floor[(line[1] + y * i), (line[0] + x * i)] += 1
        if (line[0] + x * i, line[1] + y * i) == (line[2], line[3]): break
        i += 1
    pass

for line in lines:
    vents(floor, line)
print(sum([1 for x in floor.flatten() if x > 1.0]))