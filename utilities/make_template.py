#!/usr/bin/env python3
from sys import argv
from datetime import datetime
import os
import shutil

def main(day= None, year= None):
    """Makes template day{day}.py, day{day}_data.txt, day_{day}_test_data.txt from terminal,
    using `day00.py` as template file. Text files will be placed to "data" named
    folder assumed to exist in the year folder. \n

    Takes in two optional arguments: day number to spesify the file name,
    year number to spesify the folder name

    Terminal Arguments
    ---------
    :day(numbers only, opt.): Day number for the file name.
    :year(numbers only, opt.): Year number folder

    """
    if day is None:
        day = int(argv[1]) if len(argv) > 1 else datetime.now().day
    if year is None:
        year = int(argv[2]) if len(argv) > 2 else int(datetime.now().year)

    day_str = str(day).zfill(2)
    if os.path.exists(f'../{year}/day{day_str}.py'):
        print(f'Day {day} ".py"-file exits: making next day files')
        day_str = str(day+1).zfill(2)

    shutil.copy2("utilities/day00.py", f"{year}/day{day_str}.py")

    base_path = f'{year}/data/day{day_str}'
    with open(f'{base_path}_data.txt', 'w'):
        pass
    with open(f'{base_path}_test_data.txt', 'w'):
        pass
    with open(f'{base_path}_test2_data.txt', 'w'):
        pass

if __name__ == '__main__':
    main()