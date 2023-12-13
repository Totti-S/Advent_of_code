import os
def get_data(filepath, data_type='', line_is_numbers=False, has_portions=False):

    file = os.path.realpath(filepath)
    name = file.split('/')[-1].rstrip('.py')
    if data_type != '':
        data_type = '_' + data_type
    path = f'data/{name}{data_type}_data.txt'

    with open(path, "r") as f:
        if has_portions:
            data = f.read().split('\n\n')
            data = [d.split('\n') for d in data]
            if line_is_numbers:
                [[[int(x) for x in line.split()] for line in portion] for portion in data]
        else:
            data = f.read().splitlines()
            if line_is_numbers:
                data = [[int(x) for x in line.split()] for line in data]

    return data