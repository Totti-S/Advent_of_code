from utilities.get_data import get_data
import os
def main(mode='silver', data_type=''):

    file = os.path.realpath(__file__)
    name = file.split('/')[-1].rstrip('.py')
    if data_type != '':
        data_type = '_' + data_type
    path = f'data/{name}{data_type}_data.txt'

    with open(path, 'r') as f:
        data = f.read().split('\n\n')
        data = [d.split('\n') for d in data]
    print(data)

    # Horizontal-line pass
    rows = 0
    cols = 0
    for pattern in data:
        for i in range(1,len(pattern)):
            first_range = pattern[0:i]
            second_range = pattern[i:]

            max_rows = len(first_range) if len(first_range) < len(second_range) else len(second_range)
            first_range = first_range[-1*max_rows:]
            second_range = second_range[0:max_rows]
            # print('first')
            # print("\n".join(first_range))
            # print('second')
            # print( "\n".join(second_range))
            first_range.reverse()
            # print(first_range)
            all_checks = []
            for first, second in zip(first_range, second_range):
                check = all([x==y for x,y in zip(first, second)])
                all_checks.append(check)
            if all(all_checks):
                print('found', i, True)
                rows += i
                break
        else:
            # Vertical-line pass
            for i in range(1, len(pattern[0])):
                first_range = [line[:i] for line in pattern]
                second_range = [line[i:] for line in pattern]

                max_cols = len(first_range[0]) if len(first_range[0]) < len(second_range[0]) else len(second_range[0])
                first_range = [line[-1*max_cols:][::-1] for line in first_range]
                second_range = [line[0:max_cols] for line in second_range]

                all_checks = []
                for first, second in zip(first_range, second_range):
                    check = all([x==y for x,y in zip(first, second)])
                    all_checks.append(check)
                if all(all_checks):
                    print('found', i, False)
                    cols += i

                # print('first')
                # print("\n".join(first_range))
                # print('second')
                # print( "\n".join(second_range))
    
    
    silver = rows*100 + cols
    print(f'Silver : {silver}')

    rows, cols = 0, 0
    # Gold Horizontal line pass
    for pattern in data:
        # pattern = [line.replace('#', '1').replace('.', '0') for line in pattern]
        for i in range(1,len(pattern)):
            first_range = pattern[0:i]
            second_range = pattern[i:]

            max_rows = len(first_range) if len(first_range) < len(second_range) else len(second_range)
            first_range = first_range[-1*max_rows:]
            second_range = second_range[0:max_rows]

            # print('first')
            # print("\n".join(first_range))
            # print('second')
            # print( "\n".join(second_range))
            first_range.reverse()

            # print(first_range)
            all_checks = []
            for first, second in zip(first_range, second_range):
                check = len(first) - sum([x==y for x,y in zip(first, second)])
                all_checks.append(check)
            if sum(all_checks) == 1:
                print('found', i, True)
                rows += i
                break
        else:
            # Vertical-line pass
            for i in range(1, len(pattern[0])):
                first_range = [line[:i] for line in pattern]
                second_range = [line[i:] for line in pattern]

                max_cols = len(first_range[0]) if len(first_range[0]) < len(second_range[0]) else len(second_range[0])
                first_range = [line[-1*max_cols:][::-1] for line in first_range]
                second_range = [line[0:max_cols] for line in second_range]

                all_checks = []
                for first, second in zip(first_range, second_range):
                    check = len(first) - sum([x==y for x,y in zip(first, second)])
                    all_checks.append(check)
                if sum(all_checks) == 1:
                    print('found', i, False)
                    cols += i
    gold = rows*100 + cols
    print(f'Gold : {gold}')



if __name__ == "__main__":
    main()