from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    # Todays puzzle was the most straight forward so far.
    # Code comments itself
    data = [x.split(": ")[1] for x in data] # Filter out 'Card x: '

    copies = [1 for _ in range(0, len(data))]
    total = 0
    for i, line in enumerate(data):
        winning, your_numbers = [[int(num) for num in str_nums.split()] for str_nums in line.split("|")]
        card_wins = sum([(num in winning) for num in your_numbers])
        if card_wins > 0:
            total += 2** (card_wins-1)
            for x in range(1, card_wins+1):
                copies[i+x] += copies[i]
    gold_total = sum(copies)

    print(f'Silver: {total}')
    print(f'Gold: {gold_total}')

if __name__ == "__main__":
    main('gold')