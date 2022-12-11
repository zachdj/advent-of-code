from pathlib import Path
from typing import List, Callable


class Monkey:
    def __init__(
            self,
            items: List[int],
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
        self.false_monkey_idx = false_monkey_idx
        self.total_inspections: int = 0
        self.use_worry_reduction = use_worry_reduction

    def catch_item(self, item: int):
        self.items.append(item)

    def take_turn(self, monkeys):
        for item in self.items:
            item = self.operation(item)
            self.total_inspections += 1

            if self.use_worry_reduction:
                item = item // 3

            # reduce the size of worry
            item = item % (2*3*5*7*11*13*17*19)

            # throw to next monkey
            if self.test(item):
                monkeys[self.true_monkey_idx].catch_item(item)
            else:
                monkeys[self.false_monkey_idx].catch_item(item)

        self.items.clear()


def parse_monkeys(puzzle: List[str], use_worry_reduction: bool = True) -> List[Monkey]:
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
        monkeys.append(
            Monkey(starting_items, operation, test, true_monkey_idx, false_monkey_idx, use_worry_reduction)
        )

    return monkeys


def run_task(input_filepath, num_rounds: int = 20, use_worry_reduction: bool = True):
    puzzle = input_filepath.read_text().split("\n")
    monkeys: List[Monkey] = parse_monkeys(
        puzzle, use_worry_reduction=use_worry_reduction,
    )

    for turn in range(num_rounds):
        for idx, monkey in enumerate(monkeys):
            monkey.take_turn(monkeys)

    counts = sorted([monkey.total_inspections for monkey in monkeys], reverse=True)
    monkey_business = counts[0] * counts[1]

    print(f"Solution: {monkey_business}")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day11.txt"
    run_task(input_path)
    run_task(input_path, num_rounds=10_000, use_worry_reduction=False)
