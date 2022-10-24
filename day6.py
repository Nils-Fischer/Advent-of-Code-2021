import numpy as np

with open("day6.txt", "r") as f:
    population = np.array([int(i) for i in f.readline().split(",")])

def simulation(population, days):
    array =  np.array([0,np.count_nonzero(population==1), np.count_nonzero(population==2), np.count_nonzero(population==3), np.count_nonzero(population==4), np.count_nonzero(population==5), 0, 0, 0])
    for d in range(days):
        array = np.roll(array, -1)
        array[6] += array[8]
    return sum(array)


# --- Part One ---
print(simulation(population, 256))

# --- Part Two ---