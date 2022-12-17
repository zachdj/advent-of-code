from pathlib import Path
from typing import List
import numpy as np


def _read_rock_cave(puzzle: List[str]):
    """Reads the puzzle input into an array representing the rocks"""
    cave = np.zeros((200, 1000))
    cave_bottom = 0
    for line in puzzle:
        rock_pattern = line.split(" -> ")
        for r1, r2 in zip(rock_pattern[:-1], rock_pattern[1:]):
            x1, y1 = (int(coord) for coord in r1.split(","))
            x2, y2 = (int(coord) for coord in r2.split(","))
            cave[min(y1, y2):max(y1, y2)+1, min(x1, x2):max(x1, x2)+1] = 1

            cave_bottom = max(cave_bottom, y1, y2)

    floor = cave_bottom + 2
    cave[floor, :] = 1

    return cave, cave_bottom


def task1(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    cave, cave_bottom = _read_rock_cave(puzzle)
    sand_settled = 0
    done = False
    while not done:
        sand_row, sand_col = 0, 500
        # make sand fall
        while True:
            # check if falling eternally
            if sand_row > cave_bottom:
                done = True
                break
            # try to fall down
            elif not cave[sand_row + 1, sand_col]:
                sand_row += 1
            # try to fall diagonal left
            elif not cave[sand_row + 1, sand_col - 1]:
                sand_row += 1
                sand_col -= 1
            # try to fall diagonal right
            elif not cave[sand_row + 1, sand_col + 1]:
                sand_row += 1
                sand_col += 1
            # otherwise, this particle has settled
            else:
                cave[sand_row, sand_col] = 1
                sand_settled += 1
                break

    print(f"Part 1 solution: {sand_settled}")
    print("Happy Zach-is-way-behind Day!")


def task2(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    cave, cave_bottom = _read_rock_cave(puzzle)
    sand_settled = 0
    done = False
    while not done:
        sand_row, sand_col = 0, 500
        # make sand fall
        while True:
            # try to fall down
            if not cave[sand_row + 1, sand_col]:
                sand_row += 1
            # try to fall diagonal left
            elif not cave[sand_row + 1, sand_col - 1]:
                sand_row += 1
                sand_col -= 1
            # try to fall diagonal right
            elif not cave[sand_row + 1, sand_col + 1]:
                sand_row += 1
                sand_col += 1
            # otherwise, this particle has settled
            else:
                cave[sand_row, sand_col] = 1
                sand_settled += 1
                if sand_row == 0 and sand_col == 500:
                    # source has become blocked
                    done = True
                break

    print(f"Part 2 solution: {sand_settled}")
    print("Happy Zach-is-way-behind Day!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    # input_path = project_dir / "inputs" / "day14-test.txt"
    input_path = project_dir / "inputs" / "day14.txt"
    task1(input_path)
    task2(input_path)
