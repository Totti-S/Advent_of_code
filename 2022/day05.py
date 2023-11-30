from collections import deque
from copy import deepcopy
def main():
    with open("data/day05_data.txt", "r") as f:
        data = f.read()

    # Data has two parts: creates and moving order
    data = data.split("\n\n")
    creates = data[0].split('\n')
    moving_orders = data[1].split('\n')

    # We assume that we dont actually know how large the rows are
    # We do know that the number is centered with creates
    indicies = [i for i,char in enumerate(creates[-1]) if char != " "]
    crates_dict = {i : deque() for i in range(len(indicies))}

    # Start looping from last to first; fill the deque this way
    for row in reversed(creates[:-1]):
        for idx,inner_idx in enumerate(indicies):
            box = row[inner_idx]
            if box != " ":
                crates_dict[idx].append(box)

    nd_crate_dict = deepcopy(crates_dict)

    # First solution
    for order in moving_orders:
        order = order.split()
        boxes_to_move = int(order[1])
        from_column = int(order[3]) -1
        to_column = int(order[-1]) -1
        for _ in range(boxes_to_move):
            box = crates_dict[from_column].pop()
            crates_dict[to_column].append(box)

    letters = ""
    for column in crates_dict.values():
        letters += column[-1]

    print(letters, '\n')

    # Second solution
    for order in moving_orders:
        order = order.split()
        boxes_to_move = int(order[1])
        from_column = int(order[3]) -1
        to_column = int(order[-1]) -1

        removed_creates = [nd_crate_dict[from_column].pop() for _ in range(boxes_to_move)]
        for box in reversed(removed_creates):
            nd_crate_dict[to_column].append(box)

    letters = ""
    for column in nd_crate_dict.values():
        letters += column[-1]

    print(letters)


if __name__ == "__main__":
    main()