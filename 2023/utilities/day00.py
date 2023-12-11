from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    print(data)
    for line in data:
        pass
    
    total = 0
    print(f'{mode} : {total}')

if __name__ == "__main__":
    main(data_type='test')