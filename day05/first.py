from collections import defaultdict, deque

with open("input.txt") as inp:
    diagram, directions = map(lambda a: a.split("\n"), inp.read().split("\n\n"))

dp = defaultdict(deque)
num = len(diagram[-1].split())
for line in diagram[:-1]:
    for i in range(num):
        try:
            the_char = line[1 + i * 4]
            if the_char != ' ':
                dp[i + 1].append(line[1 + i * 4])
        except IndexError:
            continue

for direction in directions[:-1]:
    words = direction.split()
    quant, start, dest = int(words[1]), int(words[3]), int(words[5])
    for i in range(quant):
        dp[dest].appendleft(dp[start].popleft())

res = ""
for i in range(num):
    pot = dp[i + 1].popleft()
    res += pot if pot != "[" else ""

print(res)
