from collections import defaultdict
import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import testable

@testable(__file__, (7, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    networks: dict[str, set[str]] = defaultdict(set)
    for line in data:
        st, nd = line.split("-")
        networks[st].add(nd)
        networks[nd].add(st)

    counted_networks: set[tuple[str, str, str]] = set()
    for computer, connected_computers in networks.items():
        if not computer.startswith("t"):
            continue
        connected_computers = list(connected_computers)
        for i, other_computer in enumerate(connected_computers[:-1]):
            for second_other in connected_computers[i+1:]:
                if second_other in networks[other_computer]:
                    network = tuple(sorted([computer, other_computer, second_other]))
                    counted_networks.add(network)


    largest_set: set[tuple[str, ...]] = set()
    for computer, connected_computers in networks.items():
        all_connected = set([computer])
        connected_computers = list(connected_computers)
        for i, other_computer in enumerate(connected_computers[:-1]):
            for second_other in connected_computers[i+1:]:
                if all(second_other in networks[com] for com in all_connected) and second_other in networks[other_computer]:
                    all_connected.add(other_computer)
                    all_connected.add(second_other)

        if len(all_connected) > len(largest_set):
            largest_set = all_connected.copy()

    gold = ",".join(sorted(list(largest_set)))

    # print(counted_networks)
    silver = len(counted_networks)
    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")