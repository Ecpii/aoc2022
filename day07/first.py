from collections import defaultdict

with open("input.txt") as inp:
    directions = inp.readlines()

pwd = ''
fs = defaultdict(dict)
sizes = defaultdict(int)

for i in range(len(directions)):
    direction = directions[i]
    if direction[0] == '$':
        command = direction.split()[1]
        if command == "cd":
            location = direction.split()[-1]
            pwd = "/".join(pwd.split("/")[:-1]) \
                if location == ".." else pwd + "/" + location
            pwd = pwd.replace("//", "/")
    else:
        fs[pwd][direction.split()[1]] = direction.split()[0]


def calculate_size(dir_name: str):
    if dir_name in sizes:
        return sizes[dir_name]
    for fname, size in fs[dir_name].items():
        sizes[dir_name] += int(size) if size != "dir" else calculate_size(
            (dir_name + "/" + fname).replace("//", "/"))
    return sizes[dir_name]


calculate_size("/")

running_total = 0
for size in sizes.values():
    if size <= 100000:
        running_total += size

# print(running_total)
