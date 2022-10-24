file = open("day3.txt", "r")
oxygen, co2 = (file.read().rstrip().split("\n") for i in range(2))
for x in range(0, len(oxygen)): oxygen[x] = list(oxygen[x])
for x in range(0,len(co2)): co2[x] = list(co2[x])

for i in range(0, 12):
    char = ""
    count1 = count0 = 0
    for x in oxygen:
        if x[i] == "1": count1 += 1
        else: count0 += 1
    if count1 >= count0: char = "1"
    else: char = "0"
    for x in oxygen:
        if x[i] == char: oxygen.remove(x)

print(oxygen)