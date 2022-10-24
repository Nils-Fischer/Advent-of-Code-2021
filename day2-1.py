file = open("day2.txt", "r")
text = file.read().rstrip().split("\n")
horizontal = depth = 0

for x in text:
    pos = x.rstrip().split()
    if pos[0] == "forward":
        horizontal += int(pos[1])
    elif pos[0] == "down":
        depth += int(pos[1])
    else: depth -= int(pos[1])

print(depth*horizontal)