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
    
    print(signal_sum)

    screen_output = ""
    for idx, x in enumerate(x_values):
        col_index = idx % 40 
        if col_index >= x-1 and col_index <= x+1:
            screen_output += "#" 
        else:
            screen_output += "."
    
    screen_lines = []
    for i in range(0,len(screen_output),40):
        screen_lines.append(screen_output[i:i+40])

    for line in screen_lines:
        print(line)




if __name__ == "__main__":
    main()