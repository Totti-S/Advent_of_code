def main():

    def split_tasks(tasks):
        tmp = tasks.split('-')
        return list((map(int, tmp)))

    with open("Advent_of_code22/day4_data.txt", "r") as f:
        data = f.readlines()
    
    fully_contained = 0
    overlap_sum = 0
    for pair in data:
        pair_list = pair.strip().split(',')
        
        elf_one_tasks = split_tasks(pair_list[0])
        elf_two_tasks = split_tasks(pair_list[1])
        
        if elf_one_tasks[0] == elf_two_tasks[0] or elf_one_tasks[1] == elf_two_tasks[1]:
            overlap_sum += 1
            fully_contained += 1
        else:
            task1_check = elf_one_tasks[0] < elf_two_tasks[0]
            task2_check = elf_one_tasks[1] > elf_two_tasks[1]
            
            if task1_check is task2_check:
                fully_contained += 1
                overlap_sum += 1
            elif task1_check and elf_one_tasks[1] >= elf_two_tasks[0]:
                overlap_sum += 1
            elif elf_one_tasks[0] <= elf_two_tasks[1] and task2_check: 
                overlap_sum +=1

    print(fully_contained)
    print(overlap_sum)




if __name__ == "__main__":
    main()
