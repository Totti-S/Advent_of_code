from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    cubes = ['blue', 'red', 'green']
    round_results = []
    for line in data:
        # Ignore 'Game x:' portion and split game to grabs of cubes
        grabs = line.split(":")[1].split(';')
        round = []
        for one_grab in grabs:
            result_cubes = one_grab.split(',')
            res = [0 ,0 ,0]
            for c in result_cubes:
                c = c.strip().split(" ")
                res[cubes.index(c[1])] = int(c[0])
            round.append(res)
        round_results.append(round)

    # Silver solution
    max_cubes = [14,12,13]
    total = 0
    for i, round in enumerate(round_results,1):
        could_happen = True
        for result in round:
            for r, m in zip(result, max_cubes):
                if r > m:
                    could_happen = False
        if could_happen:
            total += i
    print(total)

    # Gold solution
    total_2nd = 0
    min_cubes = []
    for round in round_results:
        power = 1
        for j, result in enumerate(round):
            if not j: # zero index resets min_cubes
                min_cubes = result
                continue
            for k in range(0,3):
                if result[k] > min_cubes[k]:
                    min_cubes[k] = result[k]
        for x in min_cubes:
            power *= x
        total_2nd += power
    print(total_2nd)


if __name__ == "__main__":
    main()
    # main('gold')