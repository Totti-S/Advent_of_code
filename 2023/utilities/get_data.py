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

def str_number_to_int(data):
    def int_or_str(val:str):
        # test = val if val[0] != "-" else val[1:]
        # return int(val) if test.isdigit() else val
        return int(val) if val.isdigit() else val
    
    return [list(map(int_or_str,line)) for line in data]