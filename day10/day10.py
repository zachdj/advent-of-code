from pathlib import Path
from collections import deque
from typing import List, Deque, Set


def task1(input_filepath):
    puzzle: List[str] = input_filepath.read_text().split("\n")
    target_cycles: Set[int] = {-20 + 40*i for i in range(1, 100)}
    instruction_queue: Deque[int] = deque()  # holds the modifier to x at each cycle

    # read the program instructions to build the queue
    for idx, line in enumerate(puzzle):
        if line == "noop":
            instruction_queue.appendleft(0)  # no-op does not change x
        else:
            _, x_delta = line.split()
            # addx Y is simulated by x += 0 in one cycle followed by x += Y in the next cycle
            instruction_queue.appendleft(0)
            instruction_queue.appendleft(int(x_delta))

    # execute the program
    x = 1
    cycle = 1
    summed_signal_strengths = 0
    while instruction_queue:
        if cycle in target_cycles:
            summed_signal_strengths += cycle * x

        x += instruction_queue.pop()
        cycle += 1

    print(f"Part 1 solution: {summed_signal_strengths}")
    print("Happy Elf Day!")


def task2(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    instruction_queue = deque()
    crt = [
        ['  ' for _ in range(40)]  # easier to read final output with spaces vs the suggested '.'
        for _ in range(6)
    ]

    for idx, line in enumerate(puzzle):
        if line == "noop":
            instruction_queue.appendleft(0)  # no-op does not change x
        else:
            _, x_delta = line.split()
            # addx Y is simulated by x += 0 in one cycle followed by x += Y in the next cycle
            instruction_queue.appendleft(0)
            instruction_queue.appendleft(int(x_delta))

    x = 1
    cycle = 0
    while instruction_queue:
        crt_row = cycle // 40  # x coordinate for the render cursor
        crt_col = cycle % 40  # y coordinate for the render cursor

        # the current pixel should be lit if it is covered by the 3-width sprite at x
        if crt_col in (x - 1, x, x + 1):
            crt[crt_row][crt_col] = '##'  # easier to read final output with '##' as opposed to '#'

        x += instruction_queue.pop()
        cycle += 1

    rendered_crt = '\n'.join([
        ''.join(row) for row in crt
    ])

    print(f"Part 2 solution: \n\n{rendered_crt}\n")
    print("Happy Dewey Decimal System Day!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day10.txt"
    task1(input_path)
    task2(input_path)
