import pprint

with open("sample.txt") as inp:
    raw_valves = inp.read().split('\n')[:-1]

total_pressure_released = 0

valves = {}
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


def highest_pressure(source: str, dest: str, history: set, time: int, targets: set):
    if not time or source in history:
        return 0
    max_pressure = 0
    if source == dest:
        print(f"Valve {source} opened!")
        for target in targets - {dest}:
            max_pressure = max(
                max_pressure,
                highest_pressure(dest, target, set(), time - 1, targets - {dest})
            )
        return valves[dest][0] * (time - 1) + max_pressure

    for path in valves[source][1]:
        # res = highest_pressure(path, dest, history | {source}, time - 1, targets)
        # if res > max_pressure:
        #     max_pressure = res
        max_pressure = max(
            max_pressure,
            highest_pressure(path, dest, history | {source}, time - 1, targets)
        )

    return max_pressure


pprint.pprint(valves)

for treasure in valuable_valves:
    total_pressure_released = max(
        total_pressure_released,
        highest_pressure('AA', treasure, set(), 30, valuable_valves)
    )
print(total_pressure_released)
