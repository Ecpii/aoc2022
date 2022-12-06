with open("input.txt") as inp:
    line = inp.read()[:-1]

l, r = 0, 14
window = set(line[l:r])

while len(window) != 14:
    l += 1
    r += 1
    window = set(line[l:r])

print(r)
