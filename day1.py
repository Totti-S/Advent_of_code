def main():
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

    print(max(top_three)) # First solution
    print(sum(top_three)) # Second solution

# Made a second solution
def main2():
    with open("Advent_of_code22/Day1_data.txt", "r") as f:
        data = f.read()

    splitted_data = data.split("\n\n")
    elf_calories = [elf.split("\n") for elf in splitted_data]
    # Conversion str -> int
    elf_calories = [(map(int, calories)) for calories in elf_calories]
    elf_sums = [sum(elf) for elf in elf_calories]
    sorted_elf_sums = sorted(elf_sums)
    
    print(sorted_elf_sums[-1])
    print(sum(sorted_elf_sums[-3:]))


if __name__ == "__main__":
    main()
    main2()
