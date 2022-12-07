from pathlib import Path
from collections import deque
from typing import Dict, List


def find_size(directory: Dict):
    size = 0
    for key, val in directory.items():
        if isinstance(val, dict):
            size += find_size(val)
        else:
            size += val

    return size


def find_maxsize_dirs(dirs: List, parent_dir: Dict, max_size=100000):
    for key, val in parent_dir.items():
        if isinstance(val, dict):
            size = find_size(val)
            if size < max_size:
                dirs.append(size)

            find_maxsize_dirs(dirs, val, max_size)


def find_minsize_dirs(dirs: List, parent_dir: Dict, min_size: float):
    for key, val in parent_dir.items():
        if isinstance(val, dict):
            size = find_size(val)
            if size >= min_size:
                dirs.append(size)

            find_minsize_dirs(dirs, val, min_size)


def build_filesystem(puzzle: List[str]) -> Dict:
    # nested dicts are directories, keys are file sizes
    filesystem = {
        "/": {}
    }

    # construct the filesystem based on the series of commands
    cursor = 0
    working_dir = filesystem
    history = deque()
    while cursor < len(puzzle):
        line = puzzle[cursor]
        if line.startswith("$ cd "):
            # manage navigation among directories
            dir_name = line[5:]
            if dir_name != "..":
                history.append(dir_name)
                working_dir = working_dir[dir_name]
            else:
                history.pop()
                working_dir = filesystem
                for elem in history:
                    working_dir = working_dir[elem]

            cursor += 1

        elif line.startswith("$ ls"):
            cursor += 1
            while cursor < len(puzzle):
                line = puzzle[cursor]
                if line.startswith("$"):
                    break
                elif line.startswith("dir "):
                    _, dir_name = line.split()
                    if not dir_name in working_dir:
                        working_dir[dir_name] = {}
                    cursor += 1
                else:
                    size, name = line.split()
                    working_dir[name] = int(size)
                    cursor += 1

    return filesystem


def task1(input_filepath):
    puzzle = input_filepath.read_text().split("\n")

    fs = build_filesystem(puzzle)

    # now we have filesystem in memory.  Find all directories with size > 100000
    qualifying_dirs = []
    find_maxsize_dirs(qualifying_dirs, fs, max_size=100000)

    print(f"Part 1 solution: {sum(qualifying_dirs)}")
    print("Mary Slimbus!")


def task2(input_filepath):
    puzzle = input_filepath.read_text().split("\n")

    fs = build_filesystem(puzzle)

    total_space = 70000000
    free_space_needed = 30000000
    unused_space = total_space - find_size(fs)
    min_size = free_space_needed - unused_space

    qualifying_dirs = []
    find_minsize_dirs(qualifying_dirs, fs, min_size=min_size)

    print(f"Part 2 solution: {min(qualifying_dirs)}")
    print("Slappy New Yaer!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day7.txt"
    task1(input_path)
    task2(input_path)