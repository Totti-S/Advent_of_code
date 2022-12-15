def main():
    with open("data/day15_data.txt", "r") as f:
        data = f.readlines()

    sensors = []
    beacons = []
    for line in data:
        line = line.split(" ")
        x_s = int(line[2].lstrip("x=").rstrip(","))
        y_s = int(line[3].lstrip("y=").rstrip(":"))

        x_b = int(line[-2].lstrip("x=").rstrip(","))
        y_b = int(line[-1].lstrip("y="))

        sensors.append((x_s,y_s))
        beacons.append((x_b,y_b))

    silver = -1
    gold = -1

    line_of_intress = 2_000_000
    not_available_line_points = set()
    for sensor, beacon in zip(sensors, beacons):
        s_x, s_y = sensor
        b_x, b_y = beacon

        dist_to_line = abs(s_y - line_of_intress)
        dist_to_beacon = abs(s_y - b_y) + abs(s_x - b_x)

        if dist_to_line < dist_to_beacon:
            leftover_dist = dist_to_beacon - dist_to_line
            not_available_line_points.update([x for x in range(s_x-leftover_dist, s_x+leftover_dist+1)])
        
    for beacon in beacons:
        x,y = beacon
        if y == line_of_intress and x in not_available_line_points:
            not_available_line_points.remove(x)

    for sensor in sensors:
        x,y = sensor
        if y == line_of_intress and x in not_available_line_points:
            not_available_line_points.remove(x)
            
    silver = len(not_available_line_points)

    # Part 2

    distances_to_beacon = []
    for sensor, beacon in zip(sensors, beacons):
        s_x, s_y = sensor
        b_x, b_y = beacon
        distances_to_beacon.append(abs(s_y - b_y) + abs(s_x - b_x))

    
    gold = -1
    upper_bound = 2*line_of_intress
    for j in range(0,upper_bound+1):
        
        i = 0
        while i <= upper_bound:
            for sensor, distance in zip(sensors, distances_to_beacon):
                s_x, s_y = sensor
                dist_to_point = abs(s_y - j) + abs(s_x - i)
                if dist_to_point <= distance:
                    i += distance - dist_to_point
                    break
            else:
                gold = i*4_000_000 + j

            if gold != -1:
                break
            i += 1
        if gold != -1:
            break

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

        
if __name__ == "__main__":
    main()