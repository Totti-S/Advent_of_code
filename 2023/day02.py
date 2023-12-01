from utilities.get_data import get_data
def main(data_type='', mode='silver'):
    data = get_data(__file__)

    # Conversion str -> int
    tmp_to_int = [(map(int, tmp)) for tmp in tmp_to_int]



if __name__ == "__main__":
    main()
    # main('gold')