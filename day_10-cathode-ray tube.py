from aocd.models import Puzzle
from aocd import submit
from aocd import numbers
from pprint import pprint

if __name__ == "__main__":
    puz = Puzzle(year=2022, day=10)

    with open('example_input.txt') as f:
        data = f.readlines()

    # data = puz.example_data.splitlines()
    data = puz.input_data.splitlines()

    data = [line.strip().split(' ') for line in data]

    instructions = []
    for line in data:
        i = [line[0], int(line[1])] if len(line) > 1 else line + [None]
        instructions.append(i)

    #part 1 #######################
    cycle, xreg, queue, strengths = 0, 1, None, {}
    rows, rowoffset = [[]], 0  # part 2
    inst = instructions.copy()
    while inst or queue:
        # part 2 #####################{
        sprite = set(range(xreg-1, xreg+2))
        if (cycle - rowoffset) in sprite:
            rows[-1].append('#')
        else:
            rows[-1].append('.')
        if cycle in range(39, 241, 40):
            rows.append([])
            rowoffset = cycle + 1
        # } ##########################
        cycle += 1
        print(f'cycle {cycle}, xreg: {xreg}', end=', ')
        if cycle in range(20, 221, 40):
            print(f'signal strength: {xreg * cycle}', end=', ')
            strengths[cycle] = xreg * cycle

        if queue:
            xreg += queue
            queue = None
        elif inst:
            if inst[0][1] != None:
                queue = inst[0][1]
                print(f' queuing instruction: {inst[0]}', end='')
            inst = inst[1:]
        print('')
    pprint(strengths)
    print(sum(strengths.values()))
    # submit(sum(strengths.values()), part='a', day=10, year=2022)
    [print(''.join(row)) for row in rows]
