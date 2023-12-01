from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    # Conversion str -> int
    tmp_to_int = [(map(int, tmp)) for tmp in tmp_to_int]



if __name__ == "__main__":
    main()