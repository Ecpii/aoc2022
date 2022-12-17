with open("input.txt") as inp:
    raw_forest = inp.read().split('\n')[:-1]

forest = [
    list(map(int, line)) for line in raw_forest
]

height = len(forest)
width = len(forest[0])


def is_visible(tree_x, tree_y):
    tree_height = forest[tree_y][tree_x]
    for x in range(tree_x - 1, -1, -1):
        if forest[tree_y][x] >= tree_height:
            break
    else:
        return True

    for x in range(tree_x + 1, width):
        if forest[tree_y][x] >= tree_height:
            break
    else:
        return True

    for y in range(tree_y - 1, -1, -1):
        if forest[y][tree_x] >= tree_height:
            break
    else:
        return True

    for y in range(tree_y + 1, height):
        if forest[y][tree_x] >= tree_height:
            break
    else:
        return True
    return False


num_visible_trees = 0

for y in range(height):
    for x in range(width):
        num_visible_trees += 1 if is_visible(x, y) else 0

print(num_visible_trees)
