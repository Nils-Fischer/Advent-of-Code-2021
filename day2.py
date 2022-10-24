# --- Day 2: Dive! ---
with open("day2.txt", "r") as f:
    txt = [s.split(" ") for s in f.read().split("\n")]

# ---Part one ---
hor = dep = 0
for x in txt:
    match x[0]:
        case "forward": hor += int(x[1])
        case "up": dep -= int(x[1])
        case "down": dep += int(x[1])
print(hor * dep)

# --- Part Two ---
hor = dep = aim = 0
for x in txt:
    match x[0]:
        case "down": aim += int(x[1])
        case "up": aim -= int(x[1])
        case "forward": 
            hor += int(x[1])
            dep += aim * int(x[1])
print(hor * dep)
