from utilities.get_data import get_data
from collections import defaultdict
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)
    data = [x.split(": ")[1] for x in data]

    copies = {x : 1 for x in range(0, len(data))}
    total = 0
    for i, line in enumerate(data):
        winning, your_numbers = line.split("|")
        winning = winning.split()
        winning = [int(tmp) for tmp in winning]

        your_numbers = your_numbers.split()
        your_numbers = [int(tmp) for tmp in your_numbers]
        if mode == 'silver':
            card_total = 0
            for num in your_numbers:
                if num in winning:
                    card_total += 1
            if card_total != 0:
                total += 2** (card_total-1)
        else:
            card_total = 0
            for num in your_numbers:
                if num in winning:
                    card_total += 1
            for x in range(1, card_total+1):
                copies[i+x] += copies[i]
    
    total = sum(copies.values())
            
    print(f'total {total}')



if __name__ == "__main__":
    main('gold')