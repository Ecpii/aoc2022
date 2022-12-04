with open("input.txt") as inp:
    lines = inp.readlines()

num_sup_sets = 0
for line in lines:
    groups = line.split(",")
    low1, hi1 = map(int, groups[0].split("-"))
    low2, hi2 = map(int, groups[1].split("-"))
    if (low2 <= low1 <= hi2) or (low2 <= hi1 <= hi2) or (low1 <= low2 <= hi1) or (low1 <= hi2 <= hi1):
        num_sup_sets += 1

print(num_sup_sets)
