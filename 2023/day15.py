from utilities.get_data import get_data
from collections import defaultdict
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    # print(data)
    if mode == 'silver':
        results = []
        for line in data:
            line = line.split(',')
            for word in line:
                current_value = 0
                for cha in word:
                    current_value += ord(cha)
                    current_value *= 17
                    current_value %= 256
                results.append(current_value)
        total = sum(results)

    else:
        boxes = defaultdict(list)   # Keep the order in the box by using list
        for line in data:           # We store lens to the box in a list like so: lens = [label, focal]
            line = line.split(',')
            for word in line:
                current_value = 0
                for i, cha in enumerate(word):
                    if cha != '=' and cha != '-':
                        current_value += ord(cha)
                        current_value *= 17
                        current_value %= 256
                    else:
                        letters = word[0:i]
                        box = boxes[current_value]
                        if cha == '=':
                            focal = int(word[-1])
                            for lens in box:
                                if lens[0] == letters:
                                    lens[1] = focal
                                    break
                            else:       # If there isn't lens labeled with current letters
                                box.append([letters, focal])
                        else:           # If charater at the end is '-'
                            i = 0
                            while i < len(box):
                                if box[i][0] == letters:
                                    box.pop(i)
                                    break
                                i += 1
        total = 0
        for box_val, box in boxes.items():
            for i, (_,focal) in enumerate(box,1):
                total += (box_val+1) * i * focal

    print(f'{mode} : {total}')

if __name__ == "__main__":
    main('gold')