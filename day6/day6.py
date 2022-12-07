from pathlib import Path
from collections import deque


def task1(input_filepath):
    puzzle = input_filepath.read_text()
    num_chars = 0
    buffer = deque(puzzle[:4], maxlen=4)
    for cursor in range(4, len(puzzle)):
        char = puzzle[cursor]
        buffer.append(char)
        if len(set(buffer)) == 4:
            num_chars = cursor + 1
            break

    print(f"Part 1 solution: {num_chars}")
    print("Cherry Mistmas!")


def task2(input_filepath):
    puzzle = input_filepath.read_text()
    num_chars = 0
    buffer = deque(puzzle[:14], maxlen=14)
    for cursor in range(4, len(puzzle)):
        char = puzzle[cursor]
        buffer.append(char)
        if len(set(buffer)) == 14:
            num_chars = cursor + 1
            break

    print(f"Part 2 solution: {num_chars}")
    print("Happy New Year!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day6.txt"
    task1(input_path)
    task2(input_path)