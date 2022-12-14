with open('input.txt') as inp:
    rucksacks = list(map(lambda a: a[:-1], inp.readlines()))

sum_pr = 0
pr = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for rs in rucksacks:
    length = len(rs)
    sing, = set(rs[:length // 2]) & set(rs[length // 2:])
    print(f"{sing = }")
    print(f"{pr.index(sing) = }")
    sum_pr += pr.index(sing)

print(sum_pr)
