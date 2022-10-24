#--- Day 1: Sonar Sweep ---
with open("day1.txt", "r") as f:
    txt = [int(x) for x in f.read().strip().split("\n")]

#--- Part one ---
count = sum([txt[i] > txt[i-1] for i in range(1,len(txt))])
print(count)
    

#--- Part two ---
count = sum([sum(txt[i-3:i]) > sum(txt[i-4:i-1]) for i in range(4,len(txt)+1)])
print(count)