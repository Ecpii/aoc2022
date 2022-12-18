import pprint

with open("input.txt") as inp:
    instructions = inp.read().split('\n')[:-1]

head_x, head_y = 0, 0
tail_x, tail_y = 0, 0
min_x, max_x, min_y, max_y = 0, 0, 0, 0

tail_visited_pos = {(0, 0)}
directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


def pretty_print():
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if x == y == 0:
                print('s', end='')
            elif (head_x, head_y) == (x, y):
                print('H', end='')
            elif (tail_x, tail_y) == (x, y):
                print('T', end='')
            else:
                print('.' if (x, y) not in tail_visited_pos else '#', end='')
        print()
    print()


def head_touching_tail():
    return abs(tail_x - head_x) < 2 and abs(tail_y - head_y) < 2


def move(dir, mag):
    global head_x
    global head_y
    global tail_x
    global tail_y
    global max_x, min_x, max_y, min_y

    for i in range(mag):
        head_x += directions[dir][0]
        head_y += directions[dir][1]
        if not head_touching_tail():
            x_step = abs(head_x - tail_x) // (head_x - tail_x) if head_x != tail_x else 0
            y_step = abs(head_y - tail_y) // (head_y - tail_y) if head_y != tail_y else 0
            tail_x += x_step
            tail_y += y_step
            max_x = max(tail_x, max_x)
            min_x = min(tail_x, min_x)
            max_y = max(tail_y, max_y)
            min_y = min(tail_y, min_y)
            tail_visited_pos.add((tail_x, tail_y))


for instruction in instructions:
    direction = instruction[0]
    magnitude = int(instruction[2:])
    move(direction, magnitude)

print(len(tail_visited_pos))
