from math import ceil

with open("sample.txt") as inp:
    raw_blueprints = inp.read().split('\n')[:-1]

blueprints = [
    # (ore_cost: cost in ore,
    # clay_cost: cost in ore,
    # obsidian_cost: cost in ore, clay,
    # geode_cost: cost in ore, obsidian
    # )
]
resources = [0, 0, 0, 0]
robots = [1, 0, 0, 0]

for raw_blueprint in raw_blueprints:
    split_blueprint = raw_blueprint.split()
    ore_costs = int(split_blueprint[6])
    clay_costs = int(split_blueprint[12])
    obsidian_costs = int(split_blueprint[18]), int(split_blueprint[21])
    geode_costs = int(split_blueprint[27]), int(split_blueprint[30])

    blueprints.append((ore_costs, clay_costs, obsidian_costs, geode_costs))

blueprint = blueprints[0]

geode_ore_cost, geode_obsidian_cost = blueprint[3]


def update_res(res, bots):
    for i in range(4):
        res[i] += bots[i]


def buy(bot_type, res, bots=robots, suppress=False):
    if not suppress:
        print(f"Buy a {bot_type} bot")
    if bot_type == "geode":
        res[0] -= blueprint[3][0]
        res[2] -= blueprint[3][1]
        bots[3] += 1
    elif bot_type == "obsidian":
        res[0] -= blueprint[2][0]
        res[1] -= blueprint[2][1]
        bots[2] += 1
    elif bot_type == 'clay':
        res[0] -= blueprint[1]
        bots[1] += 1
    else:
        res[0] -= blueprint[0]
        bots[0] += 1


def time_to_get_geode(purchase=None):
    num_turns = 1
    res = resources.copy()
    bots = robots.copy()
    if not purchase:
        if robots[2]:
            return max(
                ceil((geode_ore_cost - resources[0]) / robots[0]),
                ceil((geode_obsidian_cost - resources[2]) / robots[2])
            )
        if not robots[1]:
            return float('inf')

    update_res(res, bots)
    if purchase == 'clay':
        buy('clay', res, bots, True)

    if purchase != 'obsidian':
        while res[0] < blueprint[2][0] or res[1] < blueprint[2][1]:
            num_turns += 1
            update_res(res, bots)

        num_turns += 1
        update_res(res, bots)

    buy('obsidian', res, bots, True)

    while res[0] < geode_ore_cost or res[2] < geode_obsidian_cost:
        num_turns += 1
        update_res(res, bots)

    return num_turns


def optimize_obs():
    ore_cost, clay_cost = blueprint[2]

    while True:
        if not robots[2] \
                or geode_obsidian_cost / robots[2] > geode_ore_cost / robots[0]:
            if resources[0] < ore_cost or resources[1] < clay_cost:
                while True:
                    if not robots[1] \
                            or clay_cost / robots[1] > ore_cost / robots[0]:
                        print(f"{time_to_get_geode() = }")
                        print(f"{time_to_get_geode('clay') = }")
                        if resources[0] < blueprint[1] \
                                or time_to_get_geode('clay') >= time_to_get_geode():
                            break
                        buy('clay', resources)

                    else:
                        if resources[0] < blueprint[0]:
                            break
                        buy('ore', resources)
                break

            print(f"{time_to_get_geode() = }")
            print(f"{time_to_get_geode('obsidian') = }")
            if time_to_get_geode('obsidian') >= time_to_get_geode():
                break
            buy('obsidian', resources)

        else:
            if resources[0] < blueprint[0]:
                break
            buy('ore', resources)


def get_max_geodes(time):
    for _ in range(time):
        original_robots = robots.copy()

        while resources[0] >= geode_ore_cost and resources[2] >= geode_obsidian_cost:
            buy('geode', resources)
        optimize_obs()

        update_res(resources, original_robots)

        print(f"\n== Minute {_ + 1} ==")
        print(f"{resources = }")
        print(f"{robots = }")

    return resources[3]


print(get_max_geodes(24))
