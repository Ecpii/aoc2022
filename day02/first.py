loses_to = {
    'X': 'C', 'Y': 'A', 'Z': 'B'
}
ties = {
    'X': 'A', 'Y': 'B', 'Z': 'C'
}
pts = {
    'X': 1, 'Y': 2, 'Z': 3
}

with open("input.txt") as inp:
    matches = inp.readlines()

total_pts = 0
for match in matches:
    opp, you = match.split()
    if opp == loses_to[you]:
        total_pts += 6
    elif opp == ties[you]:
        total_pts += 3
    total_pts += pts[you]

print(total_pts)
