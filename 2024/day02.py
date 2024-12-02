import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=True)


    def check_fun(line):
        # print(line)
        jotain = None
        for num, next_num in zip(line[:-1], line[1:]):
            diff = next_num - num
            if jotain is None:
                jotain = next_num < num
            if jotain and next_num > num:
                return False
            elif not jotain and next_num < num:
                return False
            elif next_num == num:
                return False
            elif abs(diff) > 3:
                return False
        print("True")
        return True

    total = 0
    for line in data:
        jotain = None
        for num, next_num in zip(line[:-1], line[1:]):
            # print(num, next_num)
            diff = next_num - num
            if jotain is None:
                jotain = next_num < num
            if jotain and next_num > num:
                break
            elif not jotain and next_num < num:
                break
            elif next_num == num:
                break
            elif abs(diff) > 3:
                break
        else:
            # print("moit")
            total += 1
        # print(jotain)
    print(f'{mode} : {total}')
    
    total = 0
    faulty_list = []
    for j, line in enumerate(data):
        faulty_list.append([])
        jotain = None
        for i, (num, next_num) in enumerate(zip(line[:-1], line[1:])):
            print(num, next_num)
            diff = next_num - num
            if jotain is None:
                jotain = next_num < num
            if jotain and next_num > num:
                faulty_list[j].append(i)
            elif not jotain and next_num < num:
                faulty_list[j].append(i)
            elif next_num == num:
                faulty_list[j].append(i)
            elif abs(diff) > 3:
                faulty_list[j].append(i)
        if not faulty_list[j]:
            total += 1
    
    # BRUTE FORCE BABY
    for i, line in enumerate(faulty_list):
        if not len(line):
            continue
        print(data[i])
        for idx in range(len(data[i])):
            new_line = data[i].copy()
            new_line.pop(idx)
            if check_fun(new_line):
                total += 1
                break

    print(f'gold: {total}')

if __name__ == "__main__":
    print("test :", end="")
    main(data_type='test')
    main(data_type='')