from collections import deque
from statistics import median


with open("day10.txt", "r") as f:
    txt = f.read().strip().split("\n")
points_corrupt = {")": 3, "]": 57, "}": 1197, ">": 25137}
points_incomp = {"(": 1, "[": 2, "{": 3, "<": 4}
open_br = {"(": ")", "[": "]", "{": "}", "<": ">"}

# --- Part One ---
score = 0
for line in txt:
    open = deque()
    for bracket in line:
        if bracket in open_br: open.append(bracket)
        else: 
            if len(open) != 0: last = open.pop()
            else: 
                score += points_corrupt.get(bracket)
                break
            if open_br.get(last) != bracket: 
                score += points_corrupt.get(bracket)
                break
print(score)

# --- Part Two ---
scores = set()
for line in txt:
    open = deque()  
    for bracket in line:
        if bracket in open_br: open.append(bracket)
        else:
            if len(open) == 0: break
            last = open.pop()
            if open_br.get(last) != bracket: break
    else:        
        sum = 0
        for br in reversed(open):
            sum = sum*5 + points_incomp.get(br)
        scores.add(sum)

print(median(scores))
