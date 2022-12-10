from pathlib import Path
from typing import List, Set, Tuple

import numpy as np


def _follow_tail_through_grid(moves: List[str], rope_len: int = 10):
    tail_idx = rope_len - 1
    rope = [np.zeros(2, np.int32) for _ in range(rope_len)]
    tail_positions: Set[Tuple[int, int]] = {tuple(rope[tail_idx])}

    for line in moves:
        direction, num_steps = line.split()
        for step in range(int(num_steps)):
            # head is special case
            leader = rope[0]
            match direction:
                case "U":
                    leader += np.array([0, 1])
                case "D":
                    leader += np.array([0, -1])
                case "L":
                    leader += np.array([-1, 0])
                case "R":
                    leader += np.array([1, 0])

            # move every other link in the chain
            for link in range(1, rope_len):
                follower = rope[link]
                # move follower when distance is 2 or greater
                if np.linalg.norm(leader - follower) >= 2:
                    follower += np.sign(leader - follower)
                    rope[link] = follower

                leader = follower

            # keep track of the final link's unique positions
            tail_positions.add(tuple(rope[tail_idx]))

    return tail_positions


def task1(input_filepath):
    puzzle: List[str] = input_filepath.read_text().split("\n")
    tail_positions = _follow_tail_through_grid(puzzle, rope_len=10)

    print(f"Part 1 solution: {len(tail_positions)}")
    print("Happy International Anti-Corruption Day!")


def task2(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    tail_positions = _follow_tail_through_grid(puzzle, rope_len=10)

    print(f"Part 2 solution: {len(tail_positions)}")
    print("Happy Tanzania Independence Day!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day9.txt"
    task1(input_path)
    task2(input_path)
