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

    multi = 811589153
    orginal_order2 = [(n*multi,i) for n,i in orginal_order]
    moving_list2 = orginal_order2.copy()

    for _ in range(0,10):
        for num_tuple in orginal_order2:
            idx = moving_list2.index(num_tuple)
            num = num_tuple[0]
            moving_list2.pop(idx)
            inc = num % length if num > 0 else num % -length
            idx += inc
            if idx > length:
                idx = idx % length
            moving_list2.insert(idx, num_tuple)

    values2 = []
    zero_pos = moving_list2.index((0,0))
    for i in range(1000,3001, 1000):
        pos = (zero_pos + i) % (length+1)
        values2.append(moving_list2[pos][0])

    gold = sum(values2)
    print(f'Silver : {silver}')
    print(f'Gold   : {gold}')


if __name__ == "__main__":
    main()