from utilities.get_data import get_data
from utilities.alias_type import Mode

from collections import Counter

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    print(data)
    st, nd = [], []
    for line in data:
        print(line)
        j, k = line.split('   ')
        

        st.append(int((j.strip())))
        nd.append(int((k.strip())))

    st.sort()
    nd.sort()
    if mode == 'silver':
            
        distances = []
        for i, _ in enumerate(st):
            distances.append(abs(st[i] - nd[i]))
        total = sum(distances)

    elif mode == 'gold':
        occurances = Counter(nd)
        multi = [num * occurances[num] for num in st]
        total = sum(multi)

    print(f'{mode} : {total}')
if __name__ == "__main__":
    main(mode='gold', data_type='')