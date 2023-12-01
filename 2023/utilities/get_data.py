import os
def get_data(filepath, data_type=''):

    file = os.path.realpath(filepath)
    name = file.split('/')[-1].rstrip('.py')
    if data_type != '':
        data_type = '_' + data_type
    path = f'data/{name}{data_type}_data.txt'

    with open(path, "r") as f:
        data = f.read().splitlines()

    return data