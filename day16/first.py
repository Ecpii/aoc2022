import pprint
from collections import defaultdict

with open("input.txt") as inp:
    raw_valves = inp.read().split('\n')[:-1]

total_pressure_released = 0
starting_time = 30

valves = {}
paths = defaultdict(dict)
valuable_valves = set()

for raw_valve in raw_valves:
    valve_name = raw_valve[6:8]
    valves[valve_name] = (
        int(raw_valve[23:raw_valve.find(';')]),
        raw_valve[
            raw_valve.find('valve') + 6
            if raw_valve.find('valves') == -1
            else raw_valve.find('valves') + 7:
        ].split(', ')
    )

    if valves[valve_name][0]:
        valuable_valves.add(valve_name)


def find_paths(source):
    for valve in valves:
        if valve == source:
            continue
        path_length = find_shortest_path(source, valve, set())
        paths[source][valve] = path_length
        paths[valve][source] = path_length


def find_shortest_path(source, dest, history: set):
    if dest in paths[source]:
        return paths[source][dest]
    if source in history:
        return starting_time + 1
    if source == dest:
        return 0

    min_length = starting_time + 1
    for path in valves[source][1]:
        min_length = min(min_length, find_shortest_path(path, dest, history | {source}))
    return min_length + 1


def highest_pressure(source: str, dest: str, time: int, targets: set):
    time -= paths[source][dest]
    if time <= 0:
        return 0


    if not targets - {dest}:
        return valves[dest][0] * (time - 1)

    max_pressure = max([
        highest_pressure(dest, target, time - 1, targets - {dest})
        for target in targets - {dest}
    ])

    return valves[dest][0] * (time - 1) + max_pressure


for valve in valves:
    find_paths(valve)

# pprint.pprint(valves)
# pprint.pprint(paths)

for treasure in valuable_valves:
    total_pressure_released = max(
        total_pressure_released,
        highest_pressure('AA', treasure, starting_time, valuable_valves)
    )
print(total_pressure_released)
