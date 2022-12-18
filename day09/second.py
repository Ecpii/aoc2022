from first import instructions, pretty_print, directions

rope = [[0, 0] for _ in range(10)]
tail_positions = {(0, 0)}


def touching_previous(index: int) -> bool:
    return abs(rope[index - 1][0] - rope[index][0]) < 2 \
        and abs(rope[index - 1][1] - rope[index][1]) < 2


def catchup_previous(index: int):
    prev = rope[index - 1]
    curr = rope[index]
    x_step = abs(prev[0] - curr[0]) // (prev[0] - curr[0]) if prev[0] != curr[0] else 0
    y_step = abs(prev[1] - curr[1]) // (prev[1] - curr[1]) if prev[1] != curr[1] else 0

    rope[index][0] += x_step
    rope[index][1] += y_step

    if index == len(rope) - 1:
        tail_positions.add((rope[index][0], rope[index][1]))


for instruction in instructions:
    direction = instruction[0]
    magnitude = int(instruction[2:])
    for _ in range(magnitude):
        rope[0][0] += directions[direction][0]
        rope[0][1] += directions[direction][1]
        for i in range(1, len(rope)):
            if not touching_previous(i):
                catchup_previous(i)

print(len(tail_positions))
