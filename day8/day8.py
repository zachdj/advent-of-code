from pathlib import Path

import numpy as np


def task1(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    grid = np.array([[int(tree) for tree in line] for line in puzzle])
    size_x, size_y = grid.shape
    visible_trees = np.ones_like(grid)
    for x in range(1, size_x):
        for y in range(1, size_y):
            visible = False
            visible = visible or grid[x][y] > grid[:x, y].max(initial=-1)
            visible = visible or grid[x][y] > grid[x + 1 :, y].max(initial=-1)
            visible = visible or grid[x][y] > grid[x, :y].max(initial=-1)
            visible = visible or grid[x][y] > grid[x, y + 1 :].max(initial=-1)
            visible_trees[x][y] = visible

    print(f"Part 1 solution: {visible_trees.sum()}")
    print("Happy Haulidays!")


def task2(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    grid = np.array([[int(tree) for tree in line] for line in puzzle])
    size_x, size_y = grid.shape
    highest_score = -1
    for x in range(0, size_x):
        for y in range(0, size_y):
            height = grid[x][y]
            view_left = np.flip(grid[:x, y])
            if np.all(view_left < height):
                score_left = len(view_left)
            else:
                view_left = np.minimum(view_left, height)
                score_left = view_left.argmax() + 1

            view_right = grid[x + 1 :, y]
            if np.all(view_right < height):
                score_right = len(view_right)
            else:
                view_right = np.minimum(view_right, height)
                score_right = view_right.argmax() + 1

            view_up = np.flip(grid[x, :y])
            if np.all(view_up < height):
                score_up = len(view_up)
            else:
                view_up = np.minimum(view_up, height)
                score_up = view_up.argmax() + 1

            view_down = grid[x, y + 1 :]
            if np.all(view_down < height):
                score_down = len(view_down)
            else:
                view_down = np.minimum(view_down, height)
                score_down = view_down.argmax() + 1

            view_score = score_left * score_right * score_up * score_down
            highest_score = max(highest_score, view_score)

    print(f"Part 2 solution: {highest_score}")
    print("Cheerful Caroling!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day8.txt"
    task1(input_path)
    task2(input_path)
