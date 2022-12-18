with open("input.txt") as inp:
    commands = inp.read().split('\n')[:-1]

slide_pos = 1
cycles = 0

display = [False for _ in range(240)]


def pretty_print():
    for y in range(6):
        for x in range(40):
            print('#' if display[x + y * 40] else '.', end='')
        print()
    print()


for command in commands:
    if abs(slide_pos - cycles % 40) <= 1:
        display[cycles % 240] = True
    cycles += 1

    if command[0] == 'a':
        if abs(slide_pos - cycles % 40) <= 1:
            display[cycles % 240] = True
        cycles += 1
        slide_pos += int(command[5:])

pretty_print()
