import numpy as np

with open("day7.txt", "r") as f:
    txt = np.array(f.readline().strip().split(",")).astype(int)

# --- Part One ---
min = [sum(txt), 0]
for i in range(1, len(txt)):
    fuel = sum(abs(txt - i))
    if fuel < min[0]: min = [fuel, i]

print(min)

# --- Part Two ---
triang = np.vectorize(lambda x: x*(x+1)//2)
min = [sum(triang(txt)), 0]
for i in range(1, len(txt)):
    fuel = sum(triang(abs(txt - i)))
    if fuel < min[0]: min = [fuel, i]

print(min)
