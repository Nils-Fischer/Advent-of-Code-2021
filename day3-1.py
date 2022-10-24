file = open("day3.txt", "r")
text = file.read().rstrip().split("\n")
zero, one, gamma, epsilon = ([0 for i in range(len([char for char in text[0]]))] for i in range (4))

for x in text:
    cur = list(x)
    for y in range(0, len(cur)):
        if cur[y] == '0': zero[y] += 1
        else: one[y] += 1


for x in range(0, len(one)):
    if zero[x] > one[x]: 
        gamma[x] = 0
        epsilon[x] = 1
    else: 
        gamma[x] = 1
        epsilon[x] = 0 

consumption = int("".join(str(x) for x in gamma), 2) *  int("".join(str(x) for x in epsilon), 2)
print(consumption)
