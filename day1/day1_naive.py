""" Day 1 of https://adventofcode.com 2022

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

from pathlib import Path


def task1(input_filepath):
    """Find the elf carrying the most calories"""
    with open(input_filepath, "r") as infile:
        current_elf_calories = 0
        highest_calories = 0

        line = infile.readline()
        while line:
            if line == "\n":
                highest_calories = max(highest_calories, current_elf_calories)
                current_elf_calories = 0
            else:
                current_elf_calories += int(line)

            line = infile.readline()

    print(f"Highest-calorie elf: {highest_calories}")
    print("Merry Christmas!")


def task2(input_filepath):
    """Find the three elves carrying the most calories"""
    elf_calories = []
    with open(input_filepath, "r") as infile:
        current_elf_calories = 0
        line = infile.readline()
        while line:
            if line == "\n":
                elf_calories.append(current_elf_calories)
                current_elf_calories = 0
            else:
                current_elf_calories += int(line)

            line = infile.readline()

    elf_calories.sort(reverse=True)
    top_3 = elf_calories[:3]
    print(top_3)
    print(f"Total calories for top 3 elves: {sum(top_3)}")
    print("Happy Holidays!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day1.txt"
    task1(input_path)
    task2(input_path)
