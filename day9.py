def main():
    with open("day9_data.txt", "r") as f:
        data = f.readlines()

    head = [0,0]
    tail = [0,0]

    tails_positions = set()

    for line in data:
        commands = line.split(" ")
        direction, distance = commands[0], int(commands[1])
        for _ in range(distance):
            inc = 1 if direction in ["R", "U"] else -1
            if direction in ["R" ,"L"]:
                head[1] += inc
                if head[0] == tail[0] and abs(head[1] - tail[1]) == 2:
                    tail[1] += inc
                elif head[1] != tail[1] and abs(head[1] - tail[1]) == 2:
                    pos = head[1]-1 if direction == "R" else head[1]+1
                    tail = [head[0],pos]
            else:
                head[0] += inc
                if tail[1] == head[1] and abs(head[0] - tail[0]) == 2:
                    tail[0] += inc
                elif head[0] != tail[0] and abs(head[0] - tail[0]) == 2:
                    pos = head[0]-1 if direction == "U" else head[0]+1
                    tail = [pos,head[1]]

            tails_positions.add(tuple(tail))
        
    print(len(tails_positions))

    # OH SHIT, part 2 just hit
    rope = []
    for i in range(10):
        rope.append([0,0])

    tail_positions = set()

    for line in data:
        commands = line.split(" ")
        direction, distance = commands[0], int(commands[1])
        
        for _ in range(distance):
            for i,knot in enumerate(rope):
                if i == 0:  # Head moves
                    idx = 0 if direction in ["U", "D"] else 1
                    knot[idx] += 1 if direction in ["R", "U"] else -1
                else:
                    prev_knot = rope[i-1]
                    row_diff = prev_knot[0] - knot[0]
                    col_diff = prev_knot[1] - knot[1]
                    if abs(row_diff) == 2:
                        knot[0] += 1 if row_diff > 0 else -1
                        knot[1] += 1 if col_diff > 0 else -1 if col_diff else 0
                    elif abs(col_diff) == 2:
                        knot[0] += 1 if row_diff > 0 else -1 if row_diff else 0
                        knot[1] += 1 if col_diff > 0 else -1

            tail_positions.add(tuple(rope[-1]))
    print(len(tail_positions))






if __name__ == "__main__":
    main()