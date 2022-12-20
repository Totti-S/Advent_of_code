def main():
    with open("data/day20_data.txt", "r") as f:
        data = f.readlines()

    tmp_order = [int(num) for num in data]
    orginal_order = []
    nums = {}
    for num in tmp_order:
        if num not in nums:
            nums[num] = 0
        orginal_order.append((num, nums[num]))
        nums[num] +=1


    moving_list = orginal_order.copy()
    length = len(orginal_order) - 1


    for num_tuple in orginal_order:
        idx = moving_list.index(num_tuple)
        num = num_tuple[0]
        moving_list.pop(idx)
        inc = num % length if num > 0 else num % -length
        idx += inc
        if idx > length:
            idx = idx % length
        moving_list.insert(idx, num_tuple)

    values = []
    zero_pos = moving_list.index((0,0))
    for i in range(1000,3001, 1000):
        pos = (zero_pos + i) % (length+1)
        values.append(moving_list[pos][0])

    silver = sum(values)
    print(f'Silver : {silver}')

if __name__ == "__main__":
    main()