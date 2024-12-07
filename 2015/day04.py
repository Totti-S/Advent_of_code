import sys
sys.path.append('..')
from utilities.alias_type import Mode
from hashlib import md5

def main(mode: Mode ='silver', data_type: str = ''):
    data = "ckczppom"
    
    silver = -1
    current_hash = ""
    while not current_hash.startswith('00000'):
        silver += 1
        current_hash = md5(bytes(data + str(silver), encoding='utf-8'), usedforsecurity=False).hexdigest()

    gold = -1
    current_hash = ""
    while not current_hash.startswith('000000'):
        gold += 1
        current_hash = md5(bytes(data + str(gold), encoding='utf-8'), usedforsecurity=False).hexdigest()
        
    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main(mode="both")
    # test(main, __file__, (None, None))