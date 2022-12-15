from collections import deque, defaultdict

with open("sample.txt") as inp:
    sensors = inp.read().split("\n")[:-1]

coords = defaultdict(str)
sensors_and_radii = []
min_x, min_y = 0, 0
max_x, max_y = 0, 0


def pretty_print():
    print('     ', end='')
    for x in range(min_x, max_x + 1):
        print(str(x)[-1], end='')
    print()
    for y in range(min_y, max_y + 1):
        print(f"{y: <4}", end=' ')
        for x in range(min_x, max_x + 1):
            print(coords[x, y] if coords[x, y] else '.', end='')
        print()


#
# def map_nearby(source, radius):
#     for y in range(source[1] - radius, source[1] + radius + 1):
#         horiz_dist = radius - abs(source[1] - y)
#         for x in range(source[0] - horiz_dist, source[0] + horiz_dist + 1):
#             if coords[x, y] not in {'B', 'S', '#'}:
#                 coords[x, y] = '#'


def is_open(point):
    for sensor, radius in sensors_and_radii:
        # print(f"{sensor = }")
        # print(f"{point = }")
        # print(f"{get_manhattan_dist(point, sensor) = }")
        if get_manhattan_dist(point, sensor) <= radius and not coords[point]:
            return True
    return False


def get_manhattan_dist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point2[1] - point1[1])


# def count_open(row_n):
#     num_open = 0
#     for x in range(min_x, max_x + 1):
#         if coords[x, row_n] == '#':
#             num_open += 1
#     return num_open


def count_open(row_n):
    num_open = 0
    for x in range(min_x, max_x + 1):
        if is_open((x, row_n)):
            num_open += 1
    return num_open


for sensor in sensors:
    s_loc, b_loc = sensor.split(": ")
    s_x = int(s_loc[s_loc.find("x=") + 2:s_loc.find(",")])
    s_y = int(s_loc[s_loc.find(",") + 4:])
    b_x = int(b_loc[b_loc.find("x=") + 2:b_loc.find(",")])
    b_y = int(b_loc[b_loc.find(",") + 4:])

    dist = get_manhattan_dist((s_x, s_y), (b_x, b_y))

    max_x = max(s_x + dist, max_x)
    max_y = max(s_y + dist, max_y)
    min_x = min(s_x - dist, min_x)
    min_y = min(s_y - dist, min_y)

    coords[b_x, b_y] = 'B'
    coords[s_x, s_y] = 'S'
    sensors_and_radii.append(
        ((s_x, s_y), dist)
    )

# pretty_print()
# print(count_open(2000000))
