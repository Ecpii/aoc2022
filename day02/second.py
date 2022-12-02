win_pts = {
    'C': 1, 'B': 3, 'A': 2
}
ties = {
    'A': 1, 'B': 2, 'C': 3
}
loses_pts = {
    'A': 3, 'B': 1, 'C': 2
}
pts = {
    'X': 0, 'Y': 3, 'Z': 6
}

with open("input.txt") as inp:
    matches = inp.readlines()
# matches = ["A Y",
#            "B X",
#            "C Z"]

total_pts = 0
for match in matches:
    opp, you = match.split()
    total_pts += pts[you]
    if you == 'X':
        total_pts += loses_pts[opp]
    elif you == 'Y':
        total_pts += ties[opp]
    else:
        total_pts += win_pts[opp]

print(total_pts)
