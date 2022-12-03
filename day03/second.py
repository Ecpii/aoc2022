with open('input.txt') as inp:
    rucksacks = list(map(lambda a: a[:-1], inp.readlines()))

sum_pr = 0
pr = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0, len(rucksacks) - 2, 3):
    rs = rucksacks[i]
    rs2 = rucksacks[i + 1]
    rs3 = rucksacks[i + 2]
    sing, = set(rs) & set(rs2) & set(rs3)
    sum_pr += pr.index(sing)

print(sum_pr)
