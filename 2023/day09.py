from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)
    
    def find_prediction_val(nums):
        new_list = [nums[i]-nums[i-1] for i in range(1, len(nums))]
        if any([x != 0 for x in new_list]):
            number = find_prediction_val(new_list)
            return number + nums[-1] if mode == 'silver' else nums[0] - number
        else:
            return nums[-1]
        
    total = 0
    for line in data:
        line = [int(x) for x in line.split()]
        total += find_prediction_val(line)
    
    print(f'{mode} : {total}')

if __name__ == "__main__":
    main('gold')