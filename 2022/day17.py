import numpy as np
def main():
    with open("data/day17_data.txt", "r") as f:
        data = f.read()

    data = data.strip()
    directions = [direc for direc in data]
    chamber = np.zeros((0,7))

    heights = [1,3,3,4,2]
    highest_point = 0
    direc_pointer = 0
    for i in range(0,2022):
        rock_shape = i % 5

        # Make more chamber if rock can't be initalized
        shape_diff =  highest_point - heights[rock_shape]
        if shape_diff < 3:
            chamber = np.vstack((np.zeros((3-shape_diff, 7)), chamber))
            highest_point += 3-shape_diff

        k = shape_diff - 3 if shape_diff > 3 else 0
        # Initialize rock
        if rock_shape == 0:
            rock_pos = [[k,x] for x in range(2,6)]
        elif rock_shape == 1:
            rock_pos = [[k,3], [k+1,2], [k+1,3], [k+1,4], [k+2,3]]
        elif rock_shape == 2:
            rock_pos = [[k,4], [k+1,4], [k+2,2], [k+2,3], [k+2,4]]
        elif rock_shape == 3:
            rock_pos = [[k+x,2] for x in range(0,4)]
        else:
            rock_pos = [[k,2], [k,3], [k+1,2], [k+1,3]]

        while True:
            # 1. left-right push
            inc = -1 if directions[direc_pointer] == "<" else 1
            direc_pointer += 1
            direc_pointer %= len(directions)

            tmp_pos = [[y,x+inc] for y,x in rock_pos]
            for row, col in tmp_pos:
                if not (0 <= col <= 6): break    # Hit the wall
                if chamber[row, col]: break  # Rock in way
            else:
                rock_pos = tmp_pos
            direc_pointer += 0
            # 2. Gravity thing
            tmp_pos = [[y+1,x] for y,x in rock_pos]
            for row, col in tmp_pos:
                if row == np.shape(chamber)[0] or chamber[row, col]: # Hit the floor or rock in way
                    highest_point = rock_pos[0][0] if rock_pos[0][0] < highest_point else highest_point
                    for row, col in rock_pos:
                        chamber[row, col] = i+1
                    break
            else:
                rock_pos = tmp_pos
                tmp_chamber = chamber.copy()
                for row, col in rock_pos:
                    tmp_chamber[row, col] = i+1
                continue
            break

        silver = np.shape(chamber)[0] - highest_point

    print(f'Silver: {silver}')

if __name__ == "__main__":
    main()