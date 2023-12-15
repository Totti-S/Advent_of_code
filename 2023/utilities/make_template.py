from sys import argv
from datetime import datetime
import os
import shutil
def main():
    day = argv[1] if len(argv) > 1 else datetime.now().day
    year = int(datetime.now().year)

    if os.path.exists(f'../{year}/day{day}.py'):
        print(f'Day {day} ".py"-file exits: making next day files')
        day_str = str(int(day)+1).zfill(2)
    else:
        day_str = str(day).zfill(2)


    shutil.copy2("./utilities/day00.py", f"../{year}/day{day_str}.py")

    base_str = f'../{year}/data/day'
    with open(f'../{year}/data/day{day_str}_data.txt', 'w'):
        pass
    with open(f'../{year}/data/day{day_str}_test_data.txt', 'w'):
        pass
    # os.rename(f'./{year}/{year}', f'./{year}/day{day}.py')
    # shutil.move(f'../2023/jotain.py', f'../2023/jotain2.py')


if __name__ == '__main__':
    main()