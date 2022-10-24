file = open("day4.txt","r")
boards = list(filter(None, file.read().split("\n")))
draws = boards.pop(0).split(",")

def calc(block, draw):
    sum = 0
    for x in range(0,5):
        for y in range(0,5):
            if boards[block+x][y][1] == 0:
                sum += int(boards[block+x][y][0])
    print(sum * int(draw))

for x in range(0, len(boards)):
    boards[x] = list(filter(None, boards[x].split(" ")))
    for y in range(0,5):
        boards[x][y] = [boards[x][y], 0]


def test():
    for x in draws:
        for i in range(0, len(boards)-5, 4):
            for y in range(0,5):
                for z in range(0,5):
                    if boards[i+y][z][0] == x:  
                        boards[i+y][z][1] = 1
                        print("g")

                    if boards[i+z][y][0] == x:  boards[i+z][y][1] = 1
            sumh = sumv = 0
            for y in range(0,5):
                for z in range(0,5):
                    if boards[i+y][z][1] == 1:  
                        sumh += 1
                        if sumh == 5: 
                            print(boards)
                            """ calc(i, x) """
                            return
                    if boards[i+z][y][1] == 1:  
                        sumh += 1
                        if sumv == 5: 
                            print(boards)
                            """ calc(i, x) """
                            return

test()


            
