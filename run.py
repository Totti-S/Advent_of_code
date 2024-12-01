#!/usr/bin/env python3
from sys import argv
from datetime import datetime
import os
import subprocess

def main():
    """
    Terminal Arguments
    ---------
    :day(numbers only, opt.): Day number for the file name.
    :year(numbers only, opt.): Year number folder

    """
    day = argv[1] if len(argv) > 1 else datetime.now().day
    year = argv[2] if len(argv) > 2 else int(datetime.now().year)
    day = str(int(day)).zfill(2)

    if os.path.exists((exe := f'{year}/day{day}.py')):
        exe = exe.lstrip(f'{year}/')
        subprocess.run(
            args=['python3', exe],
            cwd=f'/home/totti/Advent_of_code/{year}'
        )
    else:
        print(exe)
        print(f'Day {day} ".py"-file does not exits: Make new files!')

if __name__ == '__main__':
    main()