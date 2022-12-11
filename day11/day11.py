from pathlib import Path
from typing import List, Callable, Self


class Monkey:
    def __init__(
            self,
            items: List[float],
            operation: Callable,
            test: Callable,
            true_monkey_idx: int,
            false_monkey_idx: int,
            use_worry_reduction: True,
    ):
        self.items = items
        self.operation = operation
        self.test = test
        self.true_monkey_idx = true_monkey_idx
        self.true_monkey = None
        self.false_monkey_idx = false_monkey_idx
        self.false_monkey = None
        self.total_inspections: int = 0
        self.use_worry_reduction = use_worry_reduction

    def set_true_monkey(self, monkeys: List[Self]):
        self.true_monkey = monkeys[self.true_monkey_idx]

    def set_false_monkey(self, monkeys: List[Self]):
        self.false_monkey = monkeys[self.false_monkey_idx]

    def catch_item(self, item: int):
        self.items.append(item)

    def take_turn(self):
        for item in self.items:
            # inspect item
            item = self.operation(item)
            self.total_inspections += 1
            # worry goes down due to relief
            if self.use_worry_reduction:
                item = item // 3
            else:
                item = item % (2*3*5*7*11*13*17*19)
            # throw to next monkey
            if self.test(item):
                self.true_monkey.catch_item(item)
            else:
                self.false_monkey.catch_item(item)

        self.items.clear()


def task1(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    monkeys: List[Monkey] = []
    # each monkey is defined on six lines plus a blank line
    for i in range(0, len(puzzle), 7):
        monkey_spec = puzzle[i:i + 7]
        starting_items = monkey_spec[1][len("  Starting items: "):].split(', ')
        starting_items = [int(item) for item in starting_items]
        operation_spec = monkey_spec[2][len("  Operation: new = "):]
        operation = eval('lambda old: ' + operation_spec)
        divisor = monkey_spec[3][len("  Test: divisible by "):]
        test = eval(f"lambda x: x % {divisor} == 0")
        true_monkey_idx = int(monkey_spec[4][-1])
        false_monkey_idx = int(monkey_spec[5][-1])
        monkeys.append(Monkey(starting_items, operation, test, true_monkey_idx, false_monkey_idx, use_worry_reduction=True))

    for idx, monkey in enumerate(monkeys):
        monkey.set_true_monkey(monkeys)
        monkey.set_false_monkey(monkeys)

    num_turns = 20
    for turn in range(num_turns):
        for idx, monkey in enumerate(monkeys):
            monkey.take_turn()

    counts = sorted([monkey.total_inspections for monkey in monkeys], reverse=True)
    monkey_business = counts[0] * counts[1]

    print(f"Part 1 solution: {monkey_business}")
    print("!")


def task2(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    monkeys: List[Monkey] = []
    # each monkey is defined on six lines plus a blank line
    for i in range(0, len(puzzle), 7):
        monkey_spec = puzzle[i:i + 7]
        starting_items = monkey_spec[1][len("  Starting items: "):].split(', ')
        starting_items = [int(item) for item in starting_items]
        operation_spec = monkey_spec[2][len("  Operation: new = "):]
        operation = eval('lambda old: ' + operation_spec)
        divisor = monkey_spec[3][len("  Test: divisible by "):]
        test = eval(f"lambda x: x % {divisor} == 0")
        true_monkey_idx = int(monkey_spec[4][-1])
        false_monkey_idx = int(monkey_spec[5][-1])
        monkeys.append(Monkey(starting_items, operation, test, true_monkey_idx, false_monkey_idx, use_worry_reduction=False))

    for idx, monkey in enumerate(monkeys):
        monkey.set_true_monkey(monkeys)
        monkey.set_false_monkey(monkeys)

    num_turns = 10_000
    for turn in range(num_turns):
        for monkey in monkeys:
            monkey.take_turn()

    counts = sorted([monkey.total_inspections for monkey in monkeys], reverse=True)
    monkey_business = counts[0] * counts[1]

    print(f"Part 2 solution: {monkey_business}")
    print("!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day11.txt"
    task1(input_path)
    task2(input_path)
