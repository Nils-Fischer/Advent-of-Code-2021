from heapq import heappop, heappush


with open("day15.txt", "r") as f:
    array = [[int(y) for y in x] for x in f.read().strip().split("\n")]

# --- Part One ---
def route(array):
    size = len(array)
    nodes = {(x, y): array[y][x] for x in range(size) for y in range(size)}
    costs = {(0,0): 0}
    h = []
    heappush(h, (0, 0, 0))
    x, y = 0, 0
    def valid(x, y):
        return x in range(size) and y in range(size)

    while True:
        value, x, y = heappop(h)
        if x == size-1 and y == size-1:
            print(value)
            break
        for xx, yy in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if valid(xx, yy):
                cost = value + nodes[(xx,yy)]
                node = (cost, xx, yy)
                if (xx, yy) in costs and costs[(xx,yy)] <= cost:
                    continue
                heappush(h, (node))
                costs[(xx, yy)] = cost
route(array)

# --- Part Two ---
size = len(array)
for i in range(size):
    for r in range(4):
        new = []
        for x in array[i][r * size:(r+1) * (size)]:
            new.append(x%9 + 1)
        array[i].extend(new)

for r in range(4):
    for line in array[r * size:(r+1) * (size)]:
        new = []
        for x in line:
            new.append(x%9 + 1)
        array.append(new)

route(array)