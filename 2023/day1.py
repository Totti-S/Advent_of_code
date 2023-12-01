def main():
    with open("data/day01_data.txt", "r") as f:
        data = f.read().splitlines()

    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    def convert_to_number(value:str, reverse:bool):
        num_index = None
        keep = None
        for i, n in enumerate(numbers,1):
            n = n[::-1] if reverse else n
            if n in value:
                tmp = value.index(n)
                if num_index is None or tmp < num_index:
                    num_index = tmp
                    keep = str(i)
        return keep
    
    # Solution: Go to first char that is a number saving all non-numbers to string.
    #           Check if the string contained a number, if yes use that instead as solution
    #           Do for both sides -> Use filpped number 'names' fro backwards comparison  

    s = 0
    for line in data:   # Forwards
        calibration_number = ''
        string = ''
        for chr in line:
            if chr.isnumeric():
                string_number = convert_to_number(string, False)
                if string_number is not None:
                    chr = string_number
                string = ''
                calibration_number += chr
                break
            else:
                string += chr
        else:
            # This is for the test case where there is no number in the string
            # Real data contains at least one number  
            string_number = convert_to_number(string, False)
            if string_number is not None:
                chr = string_number
            calibration_number += chr
    
        string = ''
        for chr in line[::-1]:  # Backwards
            if chr.isnumeric():
                string_number = convert_to_number(string, True)
                if string_number is not None:
                    chr = string_number
                string = ''
                calibration_number += chr
                break
            else:
                string += chr
        else:
            # This is for the test case where there is no number in the string
            # Real data contains at least one number  
            string_number = convert_to_number(string, True)
            if string_number is not None:
                chr = string_number
            calibration_number += chr

        s += int(calibration_number)
    
    print(s)



if __name__ == "__main__":
    main()