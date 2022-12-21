with open("sample.txt") as inp:
    raw_monkeys = inp.read().split('\n')[:-1]

monkeys = {
    monkey_string[:4]: int(monkey_string[6:])
    if ' ' not in monkey_string[6:] else monkey_string[6:]
    for monkey_string in raw_monkeys
}
inverses = {
    '*': '/', '/': '*', '+': '-', '-': '+'
}


def get_monkey_value(name):
    if type(monkeys[name]) == int:
        return monkeys[name]
    lhs, op, rhs = monkeys[name].split()
    if op == '+':
        return get_monkey_value(lhs) + get_monkey_value(rhs)
    if op == '-':
        return get_monkey_value(lhs) - get_monkey_value(rhs)
    if op == '*':
        return get_monkey_value(lhs) * get_monkey_value(rhs)
    if op == '/':
        return get_monkey_value(lhs) / get_monkey_value(rhs)


def contains_you(name):
    if name == "humn":
        return True
    if type(monkeys[name]) == int:
        return False
    lhs, _, rhs = monkeys[name].split()
    return contains_you(lhs) or contains_you(rhs)


def get_root_value():
    lhs, _, rhs = monkeys["root"].split()
    human_side = lhs if contains_you(lhs) else rhs
    monkey_side = lhs if human_side == rhs else rhs
    target_value = get_monkey_value(monkey_side)
    human_path = get_operation_path(human_side)
    while True:
        op = human_path[0]
        inverse = inverses[op]

        if human_path[1] == 'humn':
            return eval(str(target_value) + inverse + str(human_path[2]))
        if human_path[2] == 'humn':
            if op == '/':
                target_value = human_path[1] / target_value
            elif op == '-':
                target_value = human_path[1] - target_value
            else:
                target_value = eval(human_path[1] + inverse + target_value)
            return target_value

        if type(human_path[1]) != int and type(human_path[1]) != float:
            target_value = eval(str(target_value) + inverse + str(human_path[2]))
            human_path = human_path[1]
        elif type(human_path[2]) != int and type(human_path[2]) != float:
            if op == '/':
                target_value = human_path[1] / target_value
            elif op == '-':
                target_value = human_path[1] - target_value
            else:
                target_value = eval(str(target_value) + inverse + str(human_path[1]))
            human_path = human_path[2]


def get_operation_path(name):
    if name == 'humn':
        return name
    if type(monkeys[name]) == int:
        return monkeys[name]
    lhs, op, rhs = monkeys[name].split()

    res = (op, get_operation_path(lhs), get_monkey_value(rhs)) \
        if contains_you(lhs) else \
        (op, get_monkey_value(lhs), get_operation_path(rhs))
    return res


print(get_root_value())
