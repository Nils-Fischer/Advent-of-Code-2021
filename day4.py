import re
import numpy as np

with open("test.txt", "r") as f:
    txt = [[int(y) for y in x] for x in [re.findall(r"(\d+)+", x) for x in f.readlines() if x != "\n"]]
draws = txt.pop(0)
txt = np.array_split(txt, len(txt)/5)
# print(txt)

def bingo(txt, draws):
    for ind, elem in enumerate(draws):
        for x in txt:
            for i in range(4):
                if set(x[i]) <= set(draws[:ind+1]) or set(np.rot90(x)[i]) <= set(draws[:ind+1]): 
                    print(elem, i)
                    print(x.flatten())
                    return sum([s for s in x.flatten() if s not in draws[:ind+1]]) * elem

print(bingo(txt,draws))