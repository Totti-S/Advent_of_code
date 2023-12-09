from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=True)

    def predict(nums):  # Better function name from day09 -> https://github.com/knuutti/
        nxt_itr = [nums[i]-nums[i-1] for i in range(1, len(nums))]
        if sum(nxt_itr):
            return predict(nxt_itr) + nums[-1] if mode == 'silver' else nums[0] - predict(nxt_itr)
        return nums[-1]
        
    total = sum([predict(line) for line in data])
    print(f'{mode} : {total}')

if __name__ == "__main__":
    main('silver')
    main('gold')