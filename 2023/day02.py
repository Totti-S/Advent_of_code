from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    colors = ['blue', 'red', 'green']
    round_results = []
    for line in data:
        # Ignore 'Game x:' portion and split game to grabs of cubes
        grabs = line.split(": ")[1].split('; ')
        round = []
        for one_grab in grabs:
            result_cubes = one_grab.split(', ')
            result = [0, 0, 0]
            for c in result_cubes:
                amount, color = c.split()
                result[colors.index(color)] = int(amount)
            round.append(result)
        round_results.append(round)

    # Both solutions: Max cubes for silver and min cubes for gold
    from math import prod 
    max_cubes, min_cubes = [14,12,13], []
    total, gold_total = 0, 0
    for i, round in enumerate(round_results,1):
        power = 1
        could_happen = True
        for j, result in enumerate(round):
            if not j: # zero index resets min_cubes
                min_cubes = [0,0,0]
            for k in range(0,3):
                if result[k] > min_cubes[k]:
                    min_cubes[k] = result[k]
                if result[k] > max_cubes[k]:
                    could_happen = False
        
        total += i * could_happen # Not sure if better in anyway, but it's one-liner
        power *= prod(min_cubes)
        gold_total += power
    print(total)
    print(gold_total)

if __name__ == "__main__":
    main()
    # main('gold')