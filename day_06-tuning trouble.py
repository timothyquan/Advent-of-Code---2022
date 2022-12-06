from aocd.models import Puzzle
from aocd import submit


def find_distinct(signal, l):
    start, stop = 0, l
    while stop < len(signal) + l:
        if len(set(signal[start:stop])) == l:
            return stop
        start += 1
        stop += 1


if __name__ == "__main__":
    puz = Puzzle(day=6, year=2022)
    data = puz.example_data
    data = puz.input_data

    # part 1
    print(find_distinct(data, 4))
    # submit(find_distinct(data, 4), part='a', day=6, year=2022)

    # part 2
    print(find_distinct(data, 14))
    submit(find_distinct(data, 14), part='b', day=6, year=2022)
