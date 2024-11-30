from utilities.get_data import get_data
from utilities.alias_type import Mode

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    print(data)
    for line in data:
        pass

    total = 0
    print(f'{mode} : {total}')

if __name__ == "__main__":
    main(data_type='test')