from pathlib import Path
from collections import deque
from typing import List, Deque, Tuple


def _process_input(input_text) -> Tuple[List[Deque], List[str]]:
    """Turns the input text into a list of stacks and list of instructions"""
    lines = input_text.split('\n')
    # find number of stacks
    starting_line, num_stacks = 0, 0
    for idx, line in enumerate(lines):
        if line.strip().startswith('1'):
            stack_indices = line.split()
            num_stacks = max(int(idx) for idx in stack_indices)
            starting_line = idx

    stacks = [deque() for _ in range(0, num_stacks)]

    for line in lines[:starting_line]:
        # append the element for each stack
        for idx, stack in enumerate(stacks):
            # the element to be added to this stack
            # 3 spaces per stack element, plus one space in between cols
            elem_idx = 4 * idx
            elem = line[elem_idx:elem_idx+3]
            if elem.strip():
                stack.append(elem[1])

    instructions: List[str] = [line for line in lines[starting_line+2:]]

    return stacks, instructions


def _run_instruction(stacks: List[Deque], count: int, from_: int, to: int):
    """Executes the instruction of the given stacks"""
    for i in range(count):
        elem = stacks[from_].popleft()
        stacks[to].appendleft(elem)


def task1(input_filepath):
    puzzle = input_filepath.read_text()
    stacks, instructions = _process_input(puzzle)
    for instruction in instructions:
        move_count = int(instruction[instruction.index("move ")+5:instruction.index(" from")])
        from_ = int(instruction[instruction.index("from ")+5:instruction.index(" to")]) - 1
        to = int(instruction[instruction.index("to ")+3:]) - 1
        for i in range(move_count):
            elem = stacks[from_].popleft()
            stacks[to].appendleft(elem)

    # stacks now represents final config
    answer = "".join(stack.popleft() for stack in stacks)
    print(f"Part 1 solution: {answer}")
    print("Happy Chanukah!")


def task2(input_filepath):
    puzzle = input_filepath.read_text()
    stacks, instructions = _process_input(puzzle)
    for instruction in instructions:
        move_count = int(instruction[instruction.index("move ") + 5:instruction.index(" from")])
        from_ = int(instruction[instruction.index("from ") + 5:instruction.index(" to")]) - 1
        to = int(instruction[instruction.index("to ") + 3:]) - 1
        move_stack = [stacks[from_].popleft() for _ in range(move_count)]
        stacks[to].extendleft(move_stack[::-1])  # extendleft reverses the list

    # stacks now represents final config
    answer = "".join(stack.popleft() for stack in stacks)
    print(f"Part 2 solution: {answer}")
    print("Best Burra Din!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day5.txt"
    task1(input_path)
    task2(input_path)
