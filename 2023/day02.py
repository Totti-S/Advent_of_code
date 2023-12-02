from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    cubes = ['blue', 'red', 'green']
    round_results = []
    for line in data:
        line = line.split(":")
        tmp = line[1]
        grabs = tmp.split(";")
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
            for j in range(0,3):
                if result[j] > max_cubes[j]:
                    could_happen = False
        if could_happen:
            total += i
    print(total)
    
    # Gold solution
    total_2nd = 0
    for round in round_results:
        min_cubes = [-1,-1,-1]
        power = 1
        for result in round:
            for j in range(0,3):
                if min_cubes[j] == -1 or result[j] > min_cubes[j]:
                    min_cubes[j] = result[j]
        for x in min_cubes:
            power *= x
        total_2nd += power
    print(total_2nd)


if __name__ == "__main__":
    main()
    # main('gold')