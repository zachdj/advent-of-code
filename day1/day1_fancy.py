""" Day 1 of https://adventofcode.com 2022

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask:
they'd like to know how many Calories are being carried by the Elf carrying the most
Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

from bisect import insort
from pathlib import Path


def task1(input_filepath):
    """Find the elf carrying the most calories"""
    current_elf_calories = 0
    highest_calories = 0
    with open(input_filepath, "r") as infile:
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
    top3 = []
    current_elf_calories = 0
    with open(input_filepath, "r") as infile:
        line = infile.readline()
        while line:
            if line == "\n":
                insort(top3, current_elf_calories)
                top3 = top3[-3:]
                current_elf_calories = 0
            else:
                current_elf_calories += int(line)

            line = infile.readline()

    print(f"Total calories for top 3 elves: {sum(top3)}")
    print("Happy Holidays!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day1.txt"
    task1(input_path)
    task2(input_path)
