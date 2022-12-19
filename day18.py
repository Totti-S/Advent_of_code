def main():
    with open("data/day18_data.txt", "r") as f:
        data = f.readlines()

    max_dims = [0,0,0]
    total_surface = 0
    cubes = set()
    for line in data:
        line = [int(num)+1 for num in line.strip().split(",")]
        cubes.add(tuple(line))
        for i in range(0,3):
            if line[i] > max_dims[i]:
                max_dims[i] = line[i]

    for x,y,z in cubes:
        if (x+1, y, z) not in cubes:
            total_surface += 1
        if (x-1, y, z) not in cubes:
            total_surface += 1
        if (x, y+1, z) not in cubes:
            total_surface += 1
        if (x, y-1, z) not in cubes:
            total_surface += 1
        if (x, y, z+1) not in cubes:
            total_surface += 1
        if (x, y, z-1) not in cubes:
            total_surface += 1

    silver = total_surface
    air_groups = []
    for x in range(0,max_dims[0]+2):
        for y in range(0,max_dims[1]+2):
            for z in range(0, max_dims[2]+2):
                if (x, y, z) in cubes : continue
                for group in air_groups:
                    if (x+1, y, z) in group:
                        group.append((x,y,z))
                        break
                    if (x-1, y, z) in group:
                        group.append((x,y,z))
                        break
                    if (x, y+1, z) in group:
                        group.append((x,y,z))
                        break
                    if (x, y-1, z) in group:
                        group.append((x,y,z))
                        break
                    if (x, y, z+1) in group:
                        group.append((x,y,z))
                        break
                    if (x, y, z-1) in group:
                        group.append((x,y,z))
                        break
                else:
                    air_groups.append([(x,y,z)])

    tmp_groups = []
    while air_groups:
        tmp_groups.append(air_groups[0].copy())
        air_groups.pop(0)
        remove_idxs = []
        for idx, group in enumerate(air_groups):
            for x,y,z in group:
                if (x+1, y, z) in tmp_groups[-1]:
                    tmp_groups[-1].extend(group.copy())
                    remove_idxs.append(idx)
                    break
                if (x-1, y, z) in tmp_groups[-1]:
                    tmp_groups[-1].extend(group.copy())
                    remove_idxs.append(idx)
                    break
                if (x, y+1, z) in tmp_groups[-1]:
                    tmp_groups[-1].extend(group.copy())
                    remove_idxs.append(idx)
                    break
                if (x, y-1, z) in tmp_groups[-1]:
                    tmp_groups[-1].extend(group.copy())
                    remove_idxs.append(idx)
                    break
                if (x, y, z+1) in tmp_groups[-1]:
                    tmp_groups[-1].extend(group.copy())
                    remove_idxs.append(idx)
                    break
                if (x, y, z-1) in tmp_groups[-1]:
                    tmp_groups[-1].extend(group.copy())
                    remove_idxs.append(idx)
                    break

        for i,idx in enumerate(remove_idxs):
            air_groups.pop(idx - i)

    for group in tmp_groups[1:]:
        for x,y,z in group:
            if (x+1, y, z) in cubes:
                total_surface -= 1
            if (x-1, y, z) in cubes:
                total_surface -= 1
            if (x, y+1, z) in cubes:
                total_surface -= 1
            if (x, y-1, z) in cubes:
                total_surface -= 1
            if (x, y, z+1) in cubes:
                total_surface -= 1
            if (x, y, z-1) in cubes:
                total_surface -= 1

    print(f"Silver: {silver}")
    print(f"Gold: {total_surface}")

if __name__ == "__main__":
    main()