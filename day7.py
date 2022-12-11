def main():

    with open("data/day7_data.txt", "r") as f:
        data = f.readlines()
    
    class Dir:
        def __init__(self, name, dir):
            self.name = name
            self.size = 0
            self.parrent_dir = dir
            self.sub_dirs = []
            self.files = []

    class File:
        def __init__(self, name, size, f_type):
            self.name = name
            self.size = size
            self.type = f_type

    current_path = []
    master_dir = Dir("/", None)
    current_dir = None

    for line in data:
        line_info = line.split(" ")
        line_info[-1] = line_info[-1].strip()
        if line_info[0] != "$":
            if line_info[0] == "dir":
                dir_name = line_info[1]
                if not any(dir for dir in current_dir.sub_dirs if dir.name == dir_name):
                    new_dir = Dir(dir_name, current_dir)
                    current_dir.sub_dirs.append(new_dir)
                    continue
            else:
                file_info = line_info[1].split(".")
                if not any(file for file in current_dir.files if file.name == file_info[0]):
                    f_name = file_info[0]
                    f_type = file_info[1] if len(file_info) == 2 else None
                    f_size = int(line_info[0])
                    new_file = File(f_name, f_size, f_type)
                    current_dir.files.append(new_file)
                    for dir in current_path:
                        dir.size += f_size
                    continue 
        else:
            if line_info[1] == "ls":
                continue
            else:
                command = line_info[-1]
                if command == "..":
                    current_dir = current_dir.parrent_dir
                    current_path.pop()
                elif command != "/":
                    next_dir = [dir for dir in current_dir.sub_dirs if dir.name == line_info[-1]]
                    current_dir = next_dir[0]
                    current_path.append(current_dir)
                else:
                    current_dir = master_dir
                    current_path = [master_dir]

    # Now we search
    # We do it with recusive-function
    def count_small_dirs(dir, count):
        dir_sizes = [dir.size for dir in dir.sub_dirs if dir.size <= 100_000]
        count += sum(dir_sizes)
        for dir in dir.sub_dirs:
            count = count_small_dirs(dir, count)
        return count

    total_size_under_100k = count_small_dirs(master_dir, 0)
    print(total_size_under_100k)
    print()

    max_disk_space = 70_000_000
    required_space = 30_000_000
    unused_disk_space = max_disk_space - master_dir.size
    print(f'min space required to delete {required_space - unused_disk_space}')

    def find_smallest_enough(min_size, dir, unused, needed):
        dir_size_candidates_to_delete = [dir.size for dir in dir.sub_dirs if unused + dir.size >= needed]
        if not dir_size_candidates_to_delete: 
            return min_size
        smallest = min(dir_size_candidates_to_delete)
        if smallest < min_size:
            min_size = smallest
        for sub_dir in dir.sub_dirs:
            min_size = find_smallest_enough(min_size, sub_dir, unused, needed)

        return min_size

    smallest_dir = find_smallest_enough(max_disk_space, master_dir, unused_disk_space, required_space)
    print(smallest_dir)

if __name__ == "__main__":
    main()