from sqlite3 import connect


with open("day12.txt", "r") as f:
    txt = [x.split("-") for x in f.read().strip().split("\n")]

# --- Part One ---
paths = []
def route(path):
    for connection in filter(lambda x: path[-1] in x, txt):
        next = connection[0] if connection[0] != path[-1] else connection[1]
        if next == "start": continue
        if next == "end": paths.append([*path, "end"]);
        elif next.isupper() or next not in path: route([*path, next])
    return 

route(["start"])
print(len(paths))

# --- Part Two ---
paths = []

def route(path, visited):
    for connection in filter(lambda x: path[-1] in x, txt):
        next = connection[0] if connection[0] != path[-1] else connection[1]
        if next == "start": continue
        if next == "end": paths.append([*path, "end"]);
        elif next.isupper() or next not in path: route([*path, next], visited)
        elif not visited: route([*path, next], True)
    return 

route(["start"], False)
print(len(paths))