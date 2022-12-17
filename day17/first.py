from collections import defaultdict

with open("input.txt") as inp:
    jet_pattern = inp.readline()[:-1]

highest_point = 0
jet_pattern_pos = 0
board = defaultdict(str)

rocks = [
    (4, 1, [(0, 0), (1, 0), (2, 0), (3, 0)]),
    (3, 3, [(1, 0), (1, -1), (0, -1), (2, -1), (1, -2)]),
    (3, 3, [(2, 0), (2, -1), (2, -2), (1, -2), (0, -2)]),
    (1, 4, [(0, 0), (0, -1), (0, -2), (0, -3)]),
    (2, 2, [(0, 0), (0, -1), (1, 0), (1, -1)])
]


def pretty_print(rock_type, pos):
    width, height, offsets = rocks[rock_type]
    for y in range(highest_point + 3 + height, -1, -1):
        print('|', end='')
        for x in range(7):
            if pos[0] <= x < pos[0] + width \
                    and pos[1] - height < y <= pos[1]:
                print('@' if (x - pos[0], y - pos[1]) in offsets else '.', end='')
            else:
                print(board[(x, y)] if board[(x, y)] else '.', end='')
        print(f'| {y}')
    print('+-------+\n')


def is_overlapping(rock_type, pos):
    width, height, offsets = rocks[rock_type]
    if not 0 <= pos[0] <= 7 - width or pos[1] - height < -1:
        return True

    for offset in offsets:
        if board[(pos[0] + offset[0], pos[1] + offset[1])]:
            return True
    return False


def drop_rock(rock_type):
    global highest_point, jet_pattern_pos
    width, height, offsets = rocks[rock_type]
    rock_pos = [2, highest_point + height + 2]

    # pretty_print(rock_type, rock_pos)
    while True:
        horizontal_step = 1 if jet_pattern[jet_pattern_pos] == '>' else -1
        rock_pos[0] += horizontal_step
        if is_overlapping(rock_type, rock_pos):
            rock_pos[0] -= horizontal_step
        jet_pattern_pos = (jet_pattern_pos + 1) % len(jet_pattern)

        rock_pos[1] -= 1
        if is_overlapping(rock_type, rock_pos):
            rock_pos[1] += 1
            break

    for offset in offsets:
        board[(rock_pos[0] + offset[0], rock_pos[1] + offset[1])] = '#'
    highest_point = max(rock_pos[1] + 1, highest_point)


for i in range(2022):
    drop_rock(i % 5)

print(highest_point)
