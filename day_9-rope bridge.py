from aocd.models import Puzzle
from aocd import submit


def tail_follow(h, t):
    # if h[0] - h[0]:
    xdif = h[0] - t[0]
    ydif = h[1] - t[1]
    xmod = ymod = 0
    if abs(xdif) > 1:
        xmod = 1 if xdif > 0 else -1
        if abs(ydif) > 0:
            ymod = 1 if ydif > 0 else -1
    if abs(ydif) > 1:
        ymod = 1 if ydif > 0 else -1
        if abs(xdif) > 0:
            xmod = 1 if xdif > 0 else -1

    print(f'tail is modified by : {xmod, ymod}')

    t = (t[0] + xmod, t[1] + ymod)

    return t


def move_head(h, x, y):
    h = (h[0] + x, h[1] + y)
    return h


if __name__ == "__main__":
    with open('input.txt') as f:
        data = [line.strip().split() for line in f.readlines()]

    puz = Puzzle(day=9, year=2022)
    data = puz.input_data.splitlines()
    data = [line.split() for line in data]

    data = [[line[0], int(line[1])] for line in data]

    head = tail = (0, 0)

    dmap = {'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1)}
    ttrail = {tail}

    #part 1 #####################################

    # for move in data:
    #     print(f'instruction: {move} *******************')
    #     x, y = dmap[move[0]]
    #     count = move[1]
    #     for r in range(move[1]):
    #         print(f'move #{r} --------')
    #         print(f'start positions: {head, tail}')
    #         head = move_head(head, x, y)
    #         print(f'head moved: {head}')
    #         tail = tail_follow(head, tail)
    #         print(f'tail moved: {tail}')
    #         print(f'new positions: {head, tail}')
    #         ttrail.add(tail)
    # print(len(ttrail))
    #submit(len(ttrail), part='a', day=9, year=2022)

    #part 2 ###################################

    head = (0, 0)
    tails = [(0, 0) for _ in range(9)]
    ttrail = {tails[8]}
    for move in data:
        print(f'instruction: {move} *******************')
        x, y = dmap[move[0]]
        count = move[1]
        for r in range(move[1]):
            print(f'move #{r} --------')
            print(f'start positions: {head, tail}')
            head = move_head(head, x, y)
            print(f'head moved: {head}')
            lastmoved = head
            for i in range(9):
                tails[i] = tail_follow(lastmoved, tails[i])
                lastmoved = tails[i]
            print(f'tail {i} moved: {tails[i]}')
            print(f'new positions: {head, tails[i]}')
            ttrail.add(tails[8])
    print(len(ttrail))
    submit(len(ttrail), part='b', day=9, year=2022)
