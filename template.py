from pathlib import Path


def task1(input_filepath):
    puzzle = input_filepath.read_text().split("\n")

    print(f"Part 1 solution: {'derp'}")
    print("Happy International Anti-Corruption Day!")


def task2(input_filepath):
    puzzle = input_filepath.read_text().split("\n")

    print(f"Part 2 solution: {'slurp'}")
    print("Merry Tanzania Independence Day!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day.txt"
    task1(input_path)
    task2(input_path)
