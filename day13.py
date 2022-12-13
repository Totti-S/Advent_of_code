from operator import itemgetter
import numpy as np
def main():
    with open("data/day13_data.txt", "r") as f:
        data = f.read()

    def iterate_over(left,right):
        def sub_iterate(left,right):
            for sub_left, sub_right in zip(left, right):
                ans = iterate_over(sub_left,sub_right)
                if ans is not None:
                    return ans
            else:
                if len(left) == len(right):
                    return None
                else: 
                    return len(left) < len(right)

        if type(left) is type(right) is int:
            if left == right:
                return None
            else:
                return left < right
        else:
            left = [left] if type(left) is not list else left 
            right = [right] if type(right) is not list else right
            return sub_iterate(left,right)

    pairs_of_packets = [[eval(packet) for packet in pair.split("\n")] for pair in data.split("\n\n")]

    correct = []
    for i,pair in enumerate(pairs_of_packets, 1):
        ans = iterate_over(*pair)
        if ans is None and len(pair[0]) < len(pair[1]) or ans:
            correct.append(i) 
            
    print(f"Silver : {sum(correct)}")

    all_packets = []
    for packet_pair in pairs_of_packets:
        all_packets.extend(packet_pair)
    all_packets.append([[2]])   # Add dividers
    all_packets.append([[6]])
    
    # This function deconstructs the list of lists of list..... to only for 
    # a list that contains all the individual values of within the lists
    def flatten_list(elem):
        new_list = []
        for i in elem:
            if type(i) is list:
                if len(i):
                    new_list.extend(flatten_list(i))
                else:   # Replace empty with -1 -> gets priority in sorting
                    new_list.append(-1)
            else:
                new_list.append(i)
        if not len(elem):   # Replace empty with -1 -> gets priority in sorting
            new_list.append(-1) 
        return new_list

    flat_all_packets = [flatten_list(packet) for packet in all_packets]
    flat_all_packets.sort()

    # Now find the indecies of markers

    divider1 = flat_all_packets.index([2]) +1
    divider2 = flat_all_packets.index([6]) +1

    print(f"Gold: {divider1 * divider2}")

if __name__ == "__main__":
    main()