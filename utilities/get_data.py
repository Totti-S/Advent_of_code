import os
import re

def get_data(
    filepath: str | os.PathLike,
    data_type: str = '',
    line_is_numbers: bool = False,
    has_portions: bool = False
):
    file = os.path.realpath(filepath)
    file_name_list = file.split('/')
    name = file_name_list[-1].rstrip('.py')
    # year = file_name_list[-2]
    if data_type != '':
        data_type = '_' + data_type
    path = f'data/{name}{data_type}_data.txt'

    with open(path, "r") as f:
        if has_portions:
            data = f.read().split('\n\n')
            data = [d.split('\n') for d in data]
            if line_is_numbers:
                data = [[re.findall(r'\d+', line) for line in portion] for portion in data]
                data = [[list(map(int, line)) for line in portion] for portion in data]
        else:
            data = f.read().splitlines()
            if line_is_numbers:
                data = [re.findall(r'\d+', line) for line in data]
                data = [list(map(int, line)) for line in data] # Convert

    return data