from first import forest, width, height


def get_scenic_score(tree_x, tree_y):
    scores = [0, 0, 0, 0]
    tree_height = forest[tree_y][tree_x]

    for x in range(tree_x - 1, -1, -1):
        scores[0] += 1
        if forest[tree_y][x] >= tree_height:
            break

    for x in range(tree_x + 1, width):
        scores[1] += 1
        if forest[tree_y][x] >= tree_height:
            break

    for y in range(tree_y - 1, -1, -1):
        scores[2] += 1
        if forest[y][tree_x] >= tree_height:
            break

    for y in range(tree_y + 1, height):
        scores[3] += 1
        if forest[y][tree_x] >= tree_height:
            break

    return scores[0] * scores[1] * scores[2] * scores[3]


max_score = 0
for i in range(height):
    for j in range(width):
        max_score = max(get_scenic_score(j, i), max_score)

print(max_score)
