from collections import defaultdict
from first import get_manhattan_dist
import pprint

with open("input.txt") as inp:
    sensor_beacon_data = inp.read().split("\n")[:-1]

clear_areas = defaultdict(list)


def ranges_touching(range0, range1):
    return range0[0] - 1 <= range1[0] <= range0[1] + 1 or range0[0] - 1 <= range1[1] <= \
        range0[1] + 1 or \
        range1[0] - 1 <= range0[0] <= range1[1] + 1 or range1[0] - 1 <= range0[1] <= \
        range1[1] + 1


# returns True if a merge performed
def merge_ranges(row_n):
    if len(clear_areas[row_n]) <= 1:
        return False
    for i in range(len(clear_areas[row_n])):
        for j in range(i + 1, len(clear_areas[row_n])):
            if ranges_touching(clear_areas[row_n][i], clear_areas[row_n][j]):
                clear_areas[row_n][i] = (
                    min(clear_areas[row_n][i][0], clear_areas[row_n][j][0]),
                    max(clear_areas[row_n][i][1], clear_areas[row_n][j][1])
                )
                clear_areas[row_n].pop(j)
                return True
    return False


def map_clear_areas(source, radius: int):
    for y in range(source[1] - radius, source[1] + radius + 1):
        horiz_dist = radius - abs(source[1] - y)
        lower, higher = source[0] - horiz_dist, source[0] + horiz_dist
        clear_areas[y].append((lower, higher))
        while merge_ranges(y):
            pass


def find_beacon(min_x, min_y, max_x, max_y):
    width = max_x - min_x
    for y in range(min_y, max_y + 1):
        if len(clear_areas[y]) == 2:
            target_x = min(clear_areas[y][0][1], clear_areas[y][1][1]) + 1
            return target_x, y
        if (clear_areas[y][0][1] - clear_areas[y][0][0]) < width:
            target_x = max_x if 0 > clear_areas[y][0][0] else 0
            return target_x, y


for datum in sensor_beacon_data:
    s_loc, b_loc = datum.split(": ")
    s_x = int(s_loc[s_loc.find("x=") + 2:s_loc.find(",")])
    s_y = int(s_loc[s_loc.find(",") + 4:])
    b_x = int(b_loc[b_loc.find("x=") + 2:b_loc.find(",")])
    b_y = int(b_loc[b_loc.find(",") + 4:])

    dist = get_manhattan_dist((s_x, s_y), (b_x, b_y))

    map_clear_areas((s_x, s_y), dist)

# pprint.pprint(clear_areas)
beacon_coords = find_beacon(0, 0, 4000000, 4000000)
# location is at 2978645, 3249288
print(4000000 * beacon_coords[0] + beacon_coords[1])
