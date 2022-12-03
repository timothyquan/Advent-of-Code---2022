from aocd.models import Puzzle
from aocd import submit


def round_score(play):
    p1, me = play.split()
    normie = {"X": "A", "Y": "B", "Z": "C"}[me]
    plays = {"A": 1, "B": 2, "C": 3}
    score = plays[normie]
    if p1 == normie:
        score += 3
    elif (plays[p1] == plays[normie] - 1) or (plays[p1] == plays[normie] + 2):
        score += 6

    return score


def round_play(round):
    p1, wld = round.split()
    wldshift = {"Z": 1, "X": 2, "Y": 0}[wld]
    p1choice = ["A", "B", "C"].index(p1) + 1
    score = (p1choice + wldshift) % 3 if p1choice + wldshift != 3 else 3
    score += {"Z": 6, "X": 0, "Y": 3}[wld]
    return score


if __name__ == "__main__":
    puz = Puzzle(year=2022, day=2)
    example_data = puz.example_data
    input_data = puz.input_data
    scores = [round_score(line) for line in puz.input_data.split('\n')]
    # submit(sum(scores), part="a", day=2, year=2022)
    scores = [round_play(line) for line in input_data.split('\n')]
    submit(sum(scores), part="b", day=2, year=2022)
