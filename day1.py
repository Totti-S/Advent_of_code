import numpy as np
from time import perf_counter
def main():
    data = ""
    s = perf_counter()
    with open("Advent_of_code22/Day1_data.txt", "r") as f:
        data = f.readlines()
    
    calorie_counter= 0
    top_three = [-1,-1,-1]
    for calories in data:
        if calories == "\n":
            if any([calorie_counter > elf for elf in top_three]):
                top_three.remove(np.min(top_three))
                top_three.append(calorie_counter)
            calorie_counter = 0
        else:
            calorie_counter += int(calories)
    e = perf_counter()
    t = (e-s) *1000
    print(np.max(top_three), f"time: {t}")
    print(top_three)
    print(sum(top_three))

def main2():
    s = perf_counter()
    with open("Advent_of_code22/Day1_data.txt", "r") as f:
        data = f.read()

    splitted_data = data.split("\n\n")
    elf_calories = [elf.split("\n") for elf in splitted_data]
    # Conversion str -> int
    elf_calories = [(map(int, calories)) for calories in elf_calories]
    elf_sums = [sum(elf) for elf in elf_calories]
    e = perf_counter()
    t = (e-s) *1000

    sorted_elf_sums = np.sort(elf_sums)
    print(np.max(elf_sums), f"time: {t}")
    print(sorted_elf_sums[-3:]) # Instead of first the results are last three
    print(np.sum(sorted_elf_sums[-3:]))


if __name__ == "__main__":
    main()
    main2()
