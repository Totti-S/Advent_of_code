import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import test, testable

@testable(__file__, (1928, 2858))
def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    data = data[0]

    empty_spaces = []
    disk = []
    backup_disk = []
    for i, char in enumerate(data):
        if i % 2 == 0:
            disk.append([i // 2, int(char)])
            backup_disk.append([i // 2, int(char)])
        else:
            empty_spaces.append(int(char))

    disk_write_pointer = 1
    i = 0
    current_empty_space_length = empty_spaces[0]
    move_file = disk.pop()
    while i < len(empty_spaces):
        if move_file[1] == current_empty_space_length:
            disk.insert(disk_write_pointer, move_file)
            disk_write_pointer += 2
            i += 1
            if i == len(empty_spaces):
                break
            current_empty_space_length = empty_spaces[i]
            move_file = disk.pop()
        elif move_file[1] > current_empty_space_length:
            tmp_file = [move_file[0], current_empty_space_length]
            disk.insert(disk_write_pointer, tmp_file)
            move_file[1] -= current_empty_space_length
            disk_write_pointer += 2
            i += 1
            if i == len(empty_spaces):
                break
            current_empty_space_length = empty_spaces[i]
        else:
            disk.insert(disk_write_pointer, move_file)
            current_empty_space_length -= move_file[1]
            move_file = disk.pop()
            disk_write_pointer += 1

    disk.insert(disk_write_pointer, move_file)
    position = 0
    for id, space in disk:
        silver += sum(range(position, position+space)) * id
        position += space

    # For the gold solution, let's put the empty spots to the disk
    # -1 id file means empty space
    disk = backup_disk
    disk_write_pointer = 1
    for space in empty_spaces:
        disk.insert(disk_write_pointer, [-1, space])
        disk_write_pointer += 2

    # File that has the highest id is at the end of the disk
    for i in range(len(disk)-1, -1, -1):
        if disk[i][0] == -1:
            continue
        space = disk[i][1]
        # Check if there is enough space to the left of the file
        found = False
        for j, file in enumerate(disk[:i]):
            if file[0] == -1 and file[1] >= space:
                found = True
                break
        # We found space -> Move the file and adjust empty space or remove it
        # Add empty space to moved files original place. Will affect the checksum
        if found:
            file = disk.pop(i)
            disk.insert(i, [-1, file[1]])
            disk.insert(j, file)
            if file[1] == disk[j+1][1]:
                disk.pop(j+1)
            else:
                disk[j+1][1] -= file[1]

    # # Print disk as the example to confirm correct solution
    # print_str = ""
    # for id, space in disk:
    #     print_str += str(id) * space if id != -1 else "." * space
    # print(print_str)

    position = 0
    for id, space in disk:
        if id == -1:
            position += space
            continue
        gold += sum(range(position, position+space)) * id
        position += space

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")