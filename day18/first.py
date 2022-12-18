with open("input.txt") as inp:
    lines = inp.read().split('\n')[:-1]

directions = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1)
]

open_sides = 0

lava = {
    tuple(map(int, lava_pos.split(','))) for lava_pos in lines
}

for cube in lava:
    for direction in directions:
        if (cube[0] + direction[0], cube[1] + direction[1],
            cube[2] + direction[2]) not in lava:
            open_sides += 1

print(open_sides)
