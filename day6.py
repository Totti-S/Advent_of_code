import numpy as np
def main():
    with open("data/day6_data.txt", "r") as f:
        data = f.read()

    marker = -1
    for idx, char in enumerate(data):
        letters = data[idx:idx+4]
        for i in range(len(letters)):
            if letters[i] in letters[i+1:]:
                break
        else:
            marker = idx+4
        
        if marker != -1:
            break

    print(marker)

    # Second part
    marker = -1
    for idx, char in enumerate(data):
        letters = data[idx:idx+14]
        for i in range(len(letters)):
            if letters[i] in letters[i+1:]:
                break
        else:
            marker = idx+14
        
        if marker != -1:
            break

    print(marker)




if __name__ == "__main__":
    main()