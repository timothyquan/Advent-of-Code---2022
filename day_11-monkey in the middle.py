from aocd.models import Puzzle
from aocd import submit
import operator
from pprint import pprint


def worry(item, operation):
    opmap = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}

    numbers = [int(i) if i != 'old' else item for i in [
        operation[0], operation[2]]]
    new = opmap[operation[1]](*numbers)
    return new


def toss_target(item, test, t1, t2):
    return t2 if (item % test) else t1


def execute_round(monkeys):
    for i, m in enumerate(monkeys):
        print(f'processing monkey {i}.............')
        for i2, item in enumerate(m['items']):
            m['inspected_count'] += 1
            print(f'  monkey is examing {item}!!!')
            new = worry(item, m['operation'])
            print(f'    worry level is now {new}')
            new = new // 3
            print(f'    monkey is now bored, worry level reduced to {new}.')
            tt = toss_target(new, m['if'], m['then'], m['else'])
            print(f'    tossing {new} to {tt}')
            monkeys[tt]['items'].append(new)
        monkeys[i]['items'] = []


def execute_round_2(monkeys):
    divprod = 1

    for m in monkeys:
        divprod *= m['if']

    for i, m in enumerate(monkeys):
        #print(f'processing monkey {i}.............')
        for i2, item in enumerate(m['items']):
            m['inspected_count'] += 1
            #print(f'  monkey is examing {item}!!!')
            new = worry(item, m['operation'])
            #print(f'    worry level is now {new}')
            if new > 1000000:
                new = new % divprod
            # else:
            tt = toss_target(new, m['if'], m['then'], m['else'])
            #print(f'    tossing {new} to {tt}')
            monkeys[tt]['items'].append(new)
        monkeys[i]['items'] = []


if __name__ == "__main__":
    puz = Puzzle(year=2022, day=11)
    data = puz.example_data.splitlines()
    data = puz.input_data.splitlines()

    monkeys = []  # parsing monkeys##########
    for line in data:
        if line[:6] == 'Monkey':
            monkeys.append({})
            monkeys[-1]['inspected_count'] = 0
        elif 'Starting items: ' in line:
            monkeys[-1]['items'] = [int(n)
                                    for n in line[line.rfind(':') + 1:].split(', ')]
        elif 'Operation: ' in line:
            monkeys[-1]['operation'] = line[line.rfind('= ') + 2:].split(' ')
        elif 'Test: ' in line:
            monkeys[-1]['if'] = int(line[line.rfind('by ') + 3:])
        elif 'true' in line:
            monkeys[-1]['then'] = int(line[line.rfind('monkey ') + 7:])
        elif 'false' in line:
            monkeys[-1]['else'] = int(line[line.rfind('monkey ') + 7:])

    # part 1
    # for _ in range(20):
    #     execute_round(monkeys)
    # monkeybiz = operator.mul(
    #     *sorted([m['inspected_count'] for m in monkeys])[-2:])
    # print(monkeybiz)
    # submit(monkeybiz)

    # part 2
    print(list(range(1000, 10001, 1000)))
    for i in range(1, 10001):
        execute_round_2(monkeys)
        if i in [1, 20] + list(range(1000, 10001, 1000)):
            print(f'round {i}: ', end='')
            print([m['inspected_count'] for m in monkeys])
    monkeybiz = operator.mul(
        *sorted([m['inspected_count'] for m in monkeys])[-2:])
    print(monkeybiz)
    submit(monkeybiz, part='b', day=11, year=2022)
