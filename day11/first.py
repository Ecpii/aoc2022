from collections import deque

with open("input.txt") as inp:
    raw_monkeys = inp.read().split("\n\n")


class Monkey:
    def __init__(self, inp_string: str):
        _, raw_items, raw_operation, *raw_test = inp_string.split("\n")
        self.items = deque(map(int, raw_items[18:].split(", ")))

        raw_operation = raw_operation[23:]
        operator, rhs = raw_operation.split()
        if operator == '*':
            self.operation = lambda old: old * (int(rhs) if rhs != 'old' else old)
        else:
            self.operation = lambda old: old + (int(rhs) if rhs != 'old' else old)

        test_rhs = int(raw_test[0][21:])

        def _(worry):
            self.times_inspected += 1
            target_index = int(raw_test[bool(worry % test_rhs) + 1][-1])
            # print(
            #     f"Current worry level is {'not' if worry % test_rhs else ''} divisible by {test_rhs}")
            # print(f"Item with worry level {worry} is thrown to monkey {target_index}")
            monkeys[target_index].items.append(worry)

        self.test_and_throw = _

    def take_turn(self):
        while self.items:
            # print(f"\nMonkey inspects an item with a worry level of {self.items[0]}")
            considered = self.operation(self.items.popleft())
            # print(f"Worry level is up to {considered}")
            considered //= 3
            # print(
            # f"Monkey gets bored with item. Worry level is divided by 3 to {considered}"
            # )
            self.test_and_throw(considered)

    items: deque = deque()
    operation = None
    test_and_throw = None
    times_inspected: int = 0


monkeys = [
    Monkey(raw_monkey) for raw_monkey in raw_monkeys
]

for _ in range(20):
    for monkey in monkeys:
        monkey.take_turn()

if monkeys[0].times_inspected > monkeys[1].times_inspected:
    busiest = monkeys[0]
    second_busiest = monkeys[1]
else:
    busiest = monkeys[1]
    second_busiest = monkeys[0]

for monkey in monkeys[2:]:
    if monkey.times_inspected > busiest.times_inspected:
        second_busiest = busiest
        busiest = monkey
    elif monkey.times_inspected > second_busiest.times_inspected:
        second_busiest = monkey

print(busiest.times_inspected * second_busiest.times_inspected)
