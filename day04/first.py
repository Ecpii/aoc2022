with open("input.txt") as inp:
    lines = inp.readlines()

num_sup_sets = 0
for line in lines:
    groups = line.split(",")
    low1, hi1 = map(int, groups[0].split("-"))
    low2, hi2 = map(int, groups[1].split("-"))
    if (low1 <= low2 and hi1 >= hi2) or (low1 >= low2 and hi1 <= hi2):
        num_sup_sets += 1

print(num_sup_sets)
