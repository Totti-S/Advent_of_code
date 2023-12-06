from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    if mode == 'silver':
        times, distances = [line.split(':')[1].split() for line in data]
        iterations = [0] * len(times)
        i = 0
        for time, distance in zip(times, distances):
            time = int(time)
            distance = int(distance)
            for hold_time in range(1, time):
                iterations[i] += (hold_time * (time- hold_time) > distance) # Note Boolean computation
            i +=1
        
        from math import prod
        print(prod(iterations))

    else:
        time, distance = [int("".join(line.split(':')[1].split())) for line in data]
        iterations = [hold_time * (time- hold_time) > distance for hold_time in range(1, time)]
        print(sum(iterations))





if __name__ == "__main__":
    main('gold')