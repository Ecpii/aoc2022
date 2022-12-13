from collections import defaultdict

with open("sample.txt") as inp:
    comparisons = inp.read().split("\n\n")

comparisons[-1] = comparisons[-1][:-1]  # remove trailing newline


def parse_list(s: str):
    res = []
    s = s[1:-1]
    while s:
        if s[0] == ',':
            s = s[1:]
        if s[0] == '[':
            end_of_group = find_match(s)
            res.append(parse_list(s[0:end_of_group + 1]))
        else:
            end_of_group = s.find(",") if s.find(",") != -1 else len(s)
            res.append(int(s[0:end_of_group]))
        s = s[end_of_group + 1:]
    return res


def compare_lists(l, r):
    if l == r:
        return "kinda"
    if not l:
        return True
    if not r:
        return False
    if type(l[0]) is list and type(r[0]) is list:
        res = compare_lists(l[0], r[0])
    elif type(l[0]) is list and type(r[0]) is not list:
        res = compare_lists(l[0], [r[0]])
    elif type(l[0]) is not list and type(r[0]) is list:
        res = compare_lists([l[0]], r[0])
    else:
        res = l[0] < r[0] if l[0] != r[0] else "kinda"
    if res != "kinda":
        return res
    return compare_lists(l[1:], r[1:])


def find_match(s):
    depth = 1
    for i in range(1, len(s)):
        if s[i] == '[':
            depth += 1
        elif s[i] == ']':
            depth -= 1
            if depth == 0:
                return i


corrects = defaultdict(bool)
for i in range(len(comparisons)):
    if compare_lists(*map(parse_list, comparisons[i].split("\n"))):
        corrects[i + 1] = True

print(sum(corrects))
