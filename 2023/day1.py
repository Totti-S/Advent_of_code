def main():
    with open("data/day01_data.txt", "r") as f:
        data = f.readlines()

    for line in data:
        splitted_line = line.split('')
        # Conversion str -> int
        splitted_line = [(map(int, x)) for x in splitted_line]



if __name__ == "__main__":
    main()