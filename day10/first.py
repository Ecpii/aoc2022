with open("input.txt") as inp:
    commands = inp.read().split('\n')[:-1]

x = 1
cycles = 0

res = 0
marks_to_hit = {20, 60, 100, 140, 180, 220}

for command in commands:
    cycles += 1
    if cycles in marks_to_hit:
        res += x * cycles

    if command[0] == 'a':
        cycles += 1
        if cycles in marks_to_hit:
            res += x * cycles
        x += int(command[5:])

print(res)
