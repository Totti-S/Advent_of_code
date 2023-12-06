from utilities.get_data import get_data
from time import perf_counter_ns
from math import sqrt, floor, ceil
import timeit

def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    def count_iterations(time, distace):
        lower_bound = floor(((time) - sqrt(time**2 - 4*distance)) / 2)
        upper_bound = ceil(((time) + sqrt(time**2 - 4*distance)) / 2)
        return upper_bound - lower_bound - 1
    
    if mode == 'silver':
        times, distances = [line.split(':')[1].split() for line in data]
        times = [int(time) for time in times]
        distances = [int(distance) for distance in distances]

        iterations = 1
        for (time, distance) in zip(times, distances):
            iterations *= count_iterations(time, distance)

        print(iterations)

    else:
        time, distance = [int("".join(line.split(':')[1].split())) for line in data]
        iterations = count_iterations(time, distance)
        print(iterations)

if __name__ == "__main__":
    main('gold')

    # t = timeit.timeit(lambda: main('gold'), number=10_000, timer=perf_counter_ns)
    # print(f'per loop: {round((t/10_000)/1000,2)} μs')