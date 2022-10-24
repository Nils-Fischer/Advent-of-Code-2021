from collections import Counter
import re


with open("day14.txt", "r") as f:
    txt = f.read().strip()

template = re.findall(r"\A[A-Z]+", txt)[0]
pairs = re.findall(r"([A-Z]{2}) -> ([A-Z])", txt)

# --- Part One ---
prev = template
new = template[0]
rules = {x[0]: f"{x[1]}{x[0][1]}" for x in pairs}

for _ in range(10):
    for s in (f"{prev[i]}{prev[i+1]}" for i in range(len(prev)-1)):
        new += rules.get(s)
    prev = new
    new = prev[0]
    p = Counter(prev).most_common()

new = Counter(prev).most_common()
print(new[0][1] - new[-1][1])

# --- Part Two ---
rules = {x[0]: [x[0][0]+x[1], x[1]+x[0][1]] for x in pairs}
poly = [pairs[i][0] for i in range(len(pairs))]
combs = {f"{template[i]}{template[i+1]}" for i in range(len(template)-1)}
poly = {x:1 if x in combs else 0 for x in poly}

for _ in range(40):
    new = {x:0 for x in poly}
    for pair in filter(lambda x: poly[x] > 0, poly):
        count = poly[pair]
        new[rules[pair][0]] += count
        new[rules[pair][1]] += count
    poly = new

new = {x[0]:0 for x in poly} 
for s in poly:
    new[s[0]] += poly[s]
new[template[-1]] += 1
poly = Counter(new).most_common()
print(poly[0][1] - poly[-1][1])