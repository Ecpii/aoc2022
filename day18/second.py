from first import lava, directions

min_z = max_z = min_y = max_y = min_x = max_x = 0

for cube in lava:
    min_z = min(cube[2], min_z)
    min_y = min(cube[1], min_y)
    min_x = min(cube[0], min_x)
    max_z = max(cube[2], max_z)
    max_y = max(cube[1], max_y)
    max_x = max(cube[0], max_x)

steam_areas = {(min_x - 1, min_y - 1, min_z - 1)}


def touching_steam(x, y, z):
    sides_touching = 0
    for direction in directions:
        if (x + direction[0], y + direction[1], z + direction[2]) in steam_areas:
            sides_touching += 1
    return sides_touching


for _ in range(max(max_x - min_x + 1, max_y - min_y + 1, max_z - min_z + 1)):
    for z in range(min_z - 1, max_z + 2):
        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                if (x, y, z) in lava or (x, y, z) in steam_areas:
                    continue
                if touching_steam(x, y, z):
                    steam_areas.add((x, y, z))

open_faces = 0

for cube in lava:
    open_faces += touching_steam(*cube)

# everything = {(x, y, z) for x in range(min_x, max_x + 1) for z in range(min_z, max_z + 1)
#               for y in range(min_y, max_y + 1)}

# fake_open_faces = 0
# for inner_air in everything - steam_areas - cubes:
#     for direction in directions:
#         if (inner_air[0] + direction[0], inner_air[1] + direction[1],
#             inner_air[2] + direction[2]) in cubes:
#             fake_open_faces += 1
#
# print(f"{everything - steam_areas = }")
# print(f"{everything - steam_areas - cubes = }")
print(open_faces)
