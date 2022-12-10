def main():
    with open("day10_data.txt", "r") as f:
        data = f.readlines()

    x_values = [1]
    for line in data: 
        command = line.split()
        
        x_values.append(x_values[-1])
        if len(command) > 1:
            x_values.append(x_values[-1] + int(command[1]))

    signal_sum = 0
    for idx in range(20,221,40):
        signal_sum += idx*x_values[idx-1]
    
    print(signal_sum)   # Part1 solution

    screen_output = [[""] * 6]
    for idx, x in enumerate(x_values):
        row, col = divmod(idx,40) 
        screen_output[row] += "#" if x-1 <= col <= x+1 else "."

    for line in screen_output:  # Part2 solution
        print(line)

if __name__ == "__main__":
    main()