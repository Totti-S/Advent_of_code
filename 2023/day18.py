from utilities.get_data import get_data
import re
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    direction_step = dict(zip('RLUD', [(0, 1), (0, -1), (-1, 0),(1, 0)]))
    hexi = dict(zip('0123', 'RDLU'))

    current_node = (0,0)
    top_sum = 0
    total_meters = 0

    # We calculate inside of the polygon from this formula:
    # 2A = abs( sum_k=0...n-1(x_k * y_(k+1) - x_(k+1) * y_k) ),
    # where a: total area, n: number of vertex, x_k : k:th vertex x-coordinate, y_k: k:th vertex coordinate 
    for line in data:
        direction, meters, hexacode = re.match(r'(R|D|L|U) (\d+) \(#(.+)\)', line).groups()
        if mode=='gold':
            meters = int(hexacode[0:5], base=16)
            direction = hexi[hexacode[5]]
        else:
            meters = int(meters)

        step = direction_step[direction]
        next_node = (current_node[0] + step[0]*meters, current_node[1] + step[1]*meters)

        total_meters += meters
        top_sum += (current_node[0] * next_node[1] - current_node[1] * next_node[0])
        current_node = next_node
    
    total = abs(top_sum) // 2
    total += total_meters // 2 # Edge area
    total += 1 # Missing one? Maybe the starting value?
    print(f'{mode} : {total}')

if __name__ == "__main__":
    main('silver')
    main('gold')