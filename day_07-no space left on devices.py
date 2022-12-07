from aocd.models import Puzzle
from aocd import submit


class directory:
    def __init__(self, name, parent=None):
        self.files = []
        self.subdirs = []
        self.parent = parent
        self.name = name
        self.size = 0


def get_tree(input):
    root = directory('/', )
    cd = root
    for line in input:
        if line[:6] == '$ cd /':
            cd = root
        elif line[:7] == '$ cd ..':
            cd = cd.parent
        elif line[:4] == '$ cd':
            cd = [subdir for subdir in cd.subdirs if subdir.name == line[5:]][0]
        elif line[:3] == 'dir':
            name = line[4:]
            if name not in [subdir.name for subdir in cd.subdirs]:
                d = directory(line[4:], cd)
                cd.subdirs.append(d)
        elif line != '$ ls':  # files
            size, name = line.split(' ')
            if name not in [file[1] for file in cd.files]:
                cd.files.append((int(size), name))
    tree_sizes(root)
    return root


def tree_sizes(tree):
    tree.size = sum([file[0] for file in tree.files]) + \
        sum([tree_sizes(sub) for sub in tree.subdirs])
    return tree.size


def get_dirlist(tree):
    dirs = []
    for sub in tree.subdirs:
        dirs += get_dirlist(sub)
    return dirs + [tree]


if __name__ == "__main__":
    puz = Puzzle(day=7, year=2022)

    # with open("example_input.txt") as f:
    #     data = [line.strip() for line in f.readlines()]
    #    data

    data = puz.input_data.splitlines()

    tree = get_tree(data)

    # part 1:
    # directories with a total size < 100001
    ans = sum([dir.size for dir in get_dirlist(tree) if dir.size < 100001])
    print(f'part1: {ans}')
    #submit(ans, part='a', day=7, year=2022)

    # part 2:
    disk_size = 70000000
    needed_space = 30000000
    current_unused_space = disk_size - tree.size
    target_to_delete = needed_space - current_unused_space
    ans = sorted([dir.size for dir in get_dirlist(
        tree) if dir.size >= target_to_delete])[0]
    print(ans)
    submit(ans, part='b', day=7, year=2022)
