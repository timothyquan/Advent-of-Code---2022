from aocd.models import Puzzle
from aocd import submit


def count_trees(forest):
    seentrees = set()
    for i in range(4):  # from all 4 sides, 3 rotations
        for row in forest:
            highest = -1
            for tree in row:
                if tree[1] > highest:
                    highest = tree[1]
                    seentrees.add(tree)
        forest = list(zip(*forest[::-1]))

    forest = list(zip(*forest[::-1]))  # return to original state
    return seentrees


def calc_scenic_scores(forest):
    treelist = [tree for row in forest for tree in row]
    highscore = 0
    for tree in treelist:
        rightscore = 0
        for neighbor in forest[tree[0][1]][tree[0][0] + 1:]:  # to the right
            rightscore += 1
            if neighbor[1] >= tree[1]:
                break
        downscore = 0
        for c in range(tree[0][1] + 1, len(forest)):  # to the down
            downscore += 1
            if forest[c][tree[0][0]][1] >= tree[1]:
                break
        leftscore = 0
        iterforest = iter(forest[tree[0][1]][tree[0][0]::-1])
        next(iterforest)
        for neighbor in iterforest:  # to the left
            leftscore += 1
            if neighbor[1] >= tree[1]:
                break
        upscore = 0
        for c in range(tree[0][1]-1, -1, -1):  # to the up
            upscore += 1
            if forest[c][tree[0][0]][1] >= tree[1]:
                break
        totalscore = rightscore * downscore * leftscore * upscore
        highscore = totalscore if totalscore > highscore else highscore
    return highscore


if __name__ == "__main__":
    puz = Puzzle(day=8, year=2022)
    data = puz.example_data.splitlines()
    data = puz.input_data.splitlines()
    forest = [[((ci, ri), int(s)) for ci, s in enumerate(row)]
              for ri, row in enumerate(data)]

    #part 1 ##############
    seentrees = ((count_trees(forest)))
    print(len(seentrees))
    #submit(len(seentrees), part='a', day=8, year=2022)

    #part 2 ##############
    highscore = calc_scenic_scores(forest)
    print(highscore)
    submit(highscore, part='b', day=8, year=2022)
