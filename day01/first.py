import functools
with open('input.txt') as inp:
    elves = inp.read().split('\n\n')

elf_totals = []
for elf in elves:
    elf_totals.append(functools.reduce(lambda a, b: a + int(b), elf.split("\n"), 0))

elf_totals.sort()
print(sum(elf_totals[-3:]))
