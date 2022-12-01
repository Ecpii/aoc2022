import functools
with open('input.txt') as inp:
    elves = inp.read().split('\n\n')

maximum_cal = 0
for elf in elves:
    new_cal = functools.reduce(lambda a, b: a + int(b), elf.split("\n"), 0)
    if maximum_cal < new_cal:
        maximum_cal = new_cal

print(maximum_cal)
