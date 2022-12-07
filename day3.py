def main():

    with open("Advent_of_code22/day3_data.txt", "r") as f:
        data = f.readlines()

    def type_priority(item):
        ascii_a, ascii_A = ord('a'), ord('A')
        value = ord(item)
        value += 1 - ascii_a if item.islower() else 27 - ascii_A
        return value

    # First part 
    total_sum = 0
    for sack in data:
        sack = sack.strip()
        
        cutoff = int(len(sack)/2)
        st_comp = sack[0:cutoff]
        nd_comp = sack[cutoff:]

        for item in st_comp:
            if item in nd_comp:
                total_sum += type_priority(item)
                break

    print(total_sum)

    # Second part

    # First we group all the elves
    total_groups = int(len(data)/3)

    batches_sum = 0
    for idx in range(total_groups):
        start = idx * 3
        groups = data[start:start+3]
        #small optimazation: order the groups smallest to largerst
        sorted_groups = sorted(groups, key=len)
        for item in groups[0]:
            if item in groups[1] and item in groups[2]:
                batches_sum += type_priority(item)
                break
    
    print(batches_sum)

    
if __name__ == "__main__":
    main()
