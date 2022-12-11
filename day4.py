def main():

    def split_tasks(tasks):
        tmp = tasks.split('-')
        return list((map(int, tmp)))

    with open("data/day4_data.txt", "r") as f:
        data = f.readlines()
    
    fully_contained = 0
    overlap_sum = 0
    for pair in data:
        pair_list = pair.strip().split(',')
        
        elf_one_tasks = split_tasks(pair_list[0])
        elf_two_tasks = split_tasks(pair_list[1])
        
        # Solution uses few key observation:
        #   Obvious: If fully contained then it's also overlapping

        #   1. If the first tasks or the last tasks are the same then one elfs tasks is fully contained within other
        #   2. If first elfs task is smaller the second elfs task and same for to second tasks, but bigger then second elf is fully contained
        #       i. Chance the order of the elfs and you get rest of the answers
        #   3. Overlaping needs two more results: (elf1 : E1  ; elf2 : e1) -> First number elf and second task
        #       i.  E1 e1 E2 e2
        #       ii. e1 E1 e2 E2

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
