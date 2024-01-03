from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    print(data)
    hailstones = []
    for line in data:
        line = line.split(' @ ')
        positions = line[0].split(',')
        velocities = line[1].split(',')
        positions = [int(x) for x in positions]
        velocities = [int(x) for x in velocities]
        hailstones.append((*positions, *velocities))

    lower_bound = 200_000_000_000_000 if data_type == '' else 7
    upper_bound = 400_000_000_000_000 if data_type == '' else 27
    total = 0
    for i, stone in enumerate(hailstones[:-1]):
        for stone2 in hailstones[i+1:]:
            px1, py1, _, vx1, vy1, _ = stone
            px2, py2, _, vx2, vy2, _ = stone2
            if vy1*vx2 - vx1*vy2 == 0: continue
            if vy2*vx1 - vx2*vy1 == 0: continue
            intersection_x = ((py2 - py1)*vx1*vx2 + px1*vy1*vx2 - px2*vx1*vy2) / (vy1*vx2 - vx1*vy2)
            intersection_y = ((px2 - px1)*vy1*vy2 + py1*vy2*vx1 - py2*vx2*vy1) / (vy2*vx1 - vx2*vy1)

            t = (intersection_x - px1) / vx1
            if t < 0: continue
            t = (intersection_x - px2) / vx2
            if t < 0: continue

            if lower_bound <= intersection_x <= upper_bound and lower_bound <= intersection_y <= upper_bound:
                total += 1


    print(f'{mode} : {total}')

if __name__ == "__main__":
    main()