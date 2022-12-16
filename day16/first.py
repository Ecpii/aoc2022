import pprint

with open("sample.txt") as inp:
    raw_valves = inp.read().split('\n')[:-1]

total_pressure_released = 0
time_remaining = 30

valves = {}
valuable_valves = []
current_location = 'AA'

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
        valuable_valves.append(valve_name)


def pressure_of_path(source: str, dest: str, history: list, time: int):
    if source == dest:
        return valves[dest][0] * (time - 1), history + [dest]
    if source in history or not time:
        return 0, None

    max_pressure = 0
    best_path = []
    for path in valves[source][1]:
        res = pressure_of_path(path, dest, history + [source], time - 1)
        if res[0] > max_pressure:
            max_pressure = res[0]
            best_path = res[1]

    return max_pressure, best_path


while time_remaining:
    max_ppm = 0
    max_ppm_path = []
    for unopened_treasure in valuable_valves:
        cand_pressure, cand_path = pressure_of_path(
            current_location, unopened_treasure, [], time_remaining
        )
        if cand_pressure / len(cand_path) > max_ppm:
            max_ppm = cand_pressure / len(cand_path)
            max_ppm_path = cand_path
    if not max_ppm_path:
        break

    current_location = max_ppm_path[-1]
    print(f"Valve {current_location} opened!")

    time_remaining -= len(max_ppm_path) + 1
    total_pressure_released += valves[current_location][0] * time_remaining
    valuable_valves.remove(current_location)

pprint.pprint(valves)
print(total_pressure_released)
