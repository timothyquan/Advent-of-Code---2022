from aocd.models import Puzzle
from aocd import submit


def ranges(rp):
    ret = []
    for r in rp:
        ret.append(set(range(r[0], r[1] + 1, 1)))
    return ret


if __name__ == "__main__":
    puz = Puzzle(day=4, year=2022)
    data = puz.input_data.splitlines()
    #data = puz.example_data.splitlines()
    range_pairs = []
    for line in data:
        range_pairs.append([])
        for r in line.split(','):
            range_pairs[-1].append(tuple(int(i) for i in r.split('-')))

    #part 1 #########################
    subset_count = 0
    for range_pair in range_pairs:
        r1, r2 = ranges(range_pair)
        subset_count += r1.issubset(r2) or r2.issubset(r1)
    print(subset_count)
    #submit(subset_count, part='a', day=4, year=2022)

    #part 2 #########################
    overlap_count = 0
    for range_pair in range_pairs:
        r1, r2 = ranges(range_pair)
        overlap_count += len(r1.intersection(r2)) > 0
    print(overlap_count)
    submit(overlap_count, part='b', day=4, year=2022)
