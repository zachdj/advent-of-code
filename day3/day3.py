import string
from pathlib import Path


def task1(input_filepath):
    priorities = dict(
        list(zip(string.ascii_lowercase[:26], range(1, 27)))
        + list(zip(string.ascii_uppercase[:26], range(27, 53)))
    )
    with open(input_filepath, "r") as infile:
        total = 0
        rucksack = infile.readline()
        while rucksack:
            in_common = set(rucksack[: len(rucksack) // 2]).intersection(
                rucksack[len(rucksack) // 2 :]
            )
            total += priorities[next(iter(in_common))]
            rucksack = infile.readline()

    print(f"Total: {total}")
    print("Happy Yuletide!")


def task2(input_filepath):
    priorities = dict(
        list(zip(string.ascii_lowercase[:26], range(1, 27)))
        + list(zip(string.ascii_uppercase[:26], range(27, 53)))
    )
    with open(input_filepath, "r") as infile:
        total = 0
        group = []
        for line in infile:
            group.append(line.replace("\n", ""))
            if len(group) == 3:
                in_common = set.intersection(*[set(rucksack) for rucksack in group])
                total += priorities[next(iter(in_common))]
                group.clear()

    print(f"Total: {total}")
    print("Merry Chrysler!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day3.txt"
    task1(input_path)
    task2(input_path)
