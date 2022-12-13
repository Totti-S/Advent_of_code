from operator import itemgetter
import numpy as np
def main():
    with open("data/day13_data.txt", "r") as f:
        data = f.read()

    def iterate_over(left,right):
        if type(left) == type(right):
            if type(left) is int:
                if left < right:
                    return True
                elif left > right:
                    return False
                else:
                    return None
            else:
                for sub_left, sub_right in zip(left, right):
                    ans = iterate_over(sub_left,sub_right)
                    if ans is not None:
                        return ans
                else:
                    if len(left) < len(right):
                        return True
                    elif len(left) > len(right):
                        return False
                    else: return None
        else:
            left = [left] if type(left) is not list else left 
            right = [right] if type(right) is not list else right
            for sub_left, sub_right in zip(left, right):
                ans = iterate_over(sub_left,sub_right)
                if ans is not None:
                    return ans
            else:
                if len(left) < len(right):
                    return True
                elif len(left) > len(right):
                    return False
                else: return None


    packet_pairs = data.split("\n\n")
    packets = [ pair.split("\n") for pair in packet_pairs]
    for i,pair in enumerate(packets):
        for j,packet in enumerate(pair):
            packets[i][j] = eval(packet)

    correct = []

    for i,pair in enumerate(packets, 1):
        for left, right in zip(*pair):
            ans = iterate_over(left, right)
            if ans is None:
                continue
            elif ans:
                correct.append(i)
            break
        else:
            if len(pair[0]) < len(pair[1]):
                correct.append(i)


    print(f"Silver : {sum(correct)}")

    all_packets = []
    for packet_pair in packets:
        all_packets.extend([*packet_pair])
    all_packets.append([[2]])
    all_packets.append([[6]])
    

    # Replace empty with -1

    def flatten_list(elem):
        new_list = []
        for i in elem:
            if type(i) is list:
                if len(i):
                    return_value = flatten_list(i)
                    new_list.extend(flatten_list(i))
                else:
                    new_list.append(-1)
            else:
                new_list.append(i)
        if not len(elem):
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