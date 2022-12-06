from aocd.models import Puzzle
from aocd import submit
from pprint import pprint
import re


def get_moves_stacks(data):
    insts = [line for line in data if line[:4] == 'move']
    stackdrawings = [line for line in data if line.find('[') > -1]
    stacks = {}
    for stackrow in stackdrawings:
        for i in range(1, len(stackrow), 4):
            if stackrow[i] != ' ':
                stacks.setdefault((i // 4) + 1, []).insert(0, stackrow[i])

    moves = [list(map(int, re.split(' from | to ', inst[4:])))
             for inst in insts]

    return moves, stacks


if __name__ == "__main__":
    puz = Puzzle(day=5, year=2022)
    data = puz.input_data.splitlines()
    #data = puz.example_data.splitlines()

    moves, stacks = get_moves_stacks(data)

    # part 1 ####################
    for move in moves:
        for i in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())

    topcrates = [stacks[i][-1] for i in range(1, len(stacks) + 1)]
    topcrates = ''.join(topcrates)

    print(topcrates)
    #submit(topcrates, part='a', day=5, year=2022)

    moves, stacks = get_moves_stacks(data)
    # part 2 ####################
    for move in moves:
        stacks[move[2]] += (stacks[move[1]][-move[0]:])
        [stacks[move[1]].pop() for i in range(move[0])]

    topcrates = [stacks[i][-1] for i in range(1, len(stacks) + 1)]
    topcrates = ''.join(topcrates)
    print(topcrates)
    submit(topcrates, part='b', day=5, year=2022)
