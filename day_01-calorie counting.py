elves = [0]
with open('input.txt') as f:
    for line in f.readlines():
        if line == '\n':
            elves.append(0)
            continue
        elves[-1] += int(line)

# part 1
elves = sorted(elves)
print(f'The elf with the most has {elves[-1]} calories.')

# part 2
print(f'The top 3 elves have {sum(elves)[-2:]} calories total.')
