from aocd.models import Puzzle
from aocd import submit

import string


def get_common(s1, s2, s3=None):
    common = set(s1).intersection(s2)
    if s3:
        common = common.intersection(s3)
    return list(common)[0]


def get_val(s):
    p = string.ascii_lowercase + string.ascii_uppercase
    return p.index(s) + 1


if __name__ == '__main__':
    puz = Puzzle(day=3, year=2022)
    data = puz.input_data.splitlines()

    #part 1:############################
    errs = 0
    for line in data:
        c1, c2 = line[:int(len(line) / 2)], line[int(len(line) / 2):]
        common = get_common(c1, c2)
        errs += get_val(common)

    #submit(errs, part='a', day=3, year=2022)

    #part 2:###########################
    badgesum = 0
    for i in range(0, len(data), 3):
        common = get_common(*data[i:i+3])
        badgesum += get_val(common)

    submit(badgesum, part='b', day=3, year=2022)
