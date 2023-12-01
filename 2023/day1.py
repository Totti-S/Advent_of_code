def main():
    with open("data/day01_data.txt", "r") as f:
        data = f.read().splitlines()

    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    def convert_to_number(value:str, rev:bool):
        num_index = None
        keep = -1
        if rev:
            value = value[::-1]
        for i, n in enumerate(numbers,1):
            n = n[::-1] if rev else n
            if n in value:
                tmp = value.index(n)
                if num_index is None or tmp < num_index:
                    num_index = tmp
                    keep = i
        return keep

    s = 0
    for line in data:
        calibration_number = ''
        string = ''
        for chr in line:
            if chr.isnumeric():
                keep = convert_to_number(string, False)
                if keep != -1:
                    a = str(keep)
                string = ''
                calibration_number += a
                break
            else:
                string += a
        else:
            keep = convert_to_number(string, False)
            if keep != -1:
                a = str(keep)
            calibration_number += a
            keep = convert_to_number(string, True)
            if keep != -1:
                a = str(keep)
            calibration_number += a
            s += int(calibration_number)
            continue
    
        string = ''
        for chr in line[::-1]:
            if chr.isnumeric():
                keep = convert_to_number(string[::-1], True)
                if keep != -1:
                    chr = str(keep)
                string = ''
                calibration_number += a
                break
            else:
                string += a

        s += int(calibration_number)
    
    print(s)



if __name__ == "__main__":
    main()