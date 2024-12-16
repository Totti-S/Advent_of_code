import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import testable
from dataclasses import dataclass

@testable(__file__, (1928, 2858))
def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    data = data[0]

    @dataclass
    class Section:
        id: int    # If id is set to -1, it is empty space
        size: int

    def checksum(disk: list[Section]) -> int:
        s, pos = 0, 0
        for section in disk:
            if section.id == -1:
                pos += section.size
                continue
            s += sum(range(pos, pos+section.size)) * section.id
            pos += section.size
        return s
    
    def debug_print(disk: list[Section]):
        print_str = ""
        for section in disk:
            print_str += str(section.id) * section.size if section.id != -1 else "." * section.size
        print(print_str)

    def defragment_disk(disk: list[Section], silver: bool) -> list[Section]:
        j = len(disk) - 1
        while j >= 0:
            debug_print(disk)
            file = disk[j]
            if file.id == -1:
                j -= 1
                continue
            # Check if there is enough space to the left of the file
            found = False
            for i, section in enumerate(disk[:j]):
                if section.id == -1 and (section.size >= section.size or silver):
                    found = True
                    break
            # We found space -> Move the file and adjust empty space or remove it
            # Add empty space to moved files original place. Will affect the checksum
            if found:
                empty_space = disk.pop(i)
                if file.size <= empty_space.size: 
                    disk.insert(j, Section(-1, file.size))
                    disk.insert(i, file)
                    if file.size < empty_space.size:
                        disk.insert(i+1, empty_space)
                        empty_space.size -= file.size
                    disk.pop(j)
                else: # file > empty
                    empty_space.id = file.id
                    disk.insert(j, Section(-1, empty_space.size))
                    file.size -= empty_space.size
        return disk
    
    # The code starts here
    disk: list[Section] = []
    backup_disk = []
    for i, char in enumerate(data):
        id = i // 2 if not i % 2 else -1 
        disk.append(Section(id, int(char)))
        backup_disk.append(Section(id, int(char)))
    
    disk = defragment_disk(disk, True)
    silver = checksum(disk) 

    disk = backup_disk
    disk = defragment_disk(disk, False)
    gold = checksum(disk)

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", "test")