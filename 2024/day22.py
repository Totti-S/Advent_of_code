from collections import defaultdict
import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import testable

@testable(__file__, (37327623, None), (None, 23))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=True)
    silver, gold = 0, 0

    def mix_prune(secret_num: int, value: int) -> int:
        return secret_num ^ value % 16777216

    all_derivates = []
    all_prices = []
    for line in data:
        num = line[0]
        prices = [num % 10]
        derivates = [0]
        for _ in range(2000):
            num = mix_prune(num, num * 64)
            num = mix_prune(num, num // 32)
            num = mix_prune(num, num * 2048)

            prices.append(num % 10)
            derivates.append(prices[-1] - prices[-2])
        all_derivates.append(derivates)
        all_prices.append(prices)
        silver += num

    all_sequences_prices = defaultdict(int)
    for derivate, prices in zip(all_derivates, all_prices):
        sub_sequences = {}
        for i in range(1, 1996):
            sequence = tuple(derivate[i:i+4])
            if sequence not in sub_sequences:
                sub_sequences[sequence] = prices[i+3]
                all_sequences_prices[sequence] += prices[i+3]

    gold = max(all_sequences_prices.values())

    print(f'{silver = }')
    print(f'{gold = }')
if __name__ == "__main__":
    main("both", "")