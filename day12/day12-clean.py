from collections import deque
from pathlib import Path
from string import ascii_lowercase
from typing import List


def _read_height_map(puzzle: List[str]):
    letter_to_height = dict(zip(ascii_lowercase[:26], range(26)))
    hmap = {}
    start_loc = (0, 0)
    end_loc = (0, 0)
    for row, line in enumerate(puzzle):
        for col, char in enumerate(list(line)):
            if char == "S":
                hmap[(row, col)] = letter_to_height["a"]
                start_loc = (row, col)
            elif char == "E":
                hmap[(row, col)] = letter_to_height["z"]
                end_loc = (row, col)
            else:
                hmap[(row, col)] = letter_to_height[char]

    return hmap, start_loc, end_loc


def bfs(hmap, end_loc):
    """BFS from end location to all others, filtering illegal moves"""
    frontier = deque([end_loc])
    came_from = {}
    visited = {location: False for location in hmap}
    shortest_paths = {
        location: float("inf") for location, height in hmap.items() if height == 0
    }

    while frontier:
        current_loc = frontier.pop()
        visited[current_loc] = True

        row, col = current_loc
        current_height = hmap[current_loc]
        if current_height == 0:
            # reached an 'a' squared, calculate path len
            path_len = 0
            parent = current_loc
            while parent in came_from:
                parent = came_from[parent]
                path_len += 1
            shortest_paths[current_loc] = path_len

        potential_neighbors = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
        ]
        legal_moves = [
            (r, c)
            for r, c in potential_neighbors
            if (r, c) in hmap
            and (current_height - hmap[(r, c)] <= 1)
            and not visited[(r, c)]
        ]
        for neighbor in legal_moves:
            came_from[neighbor] = current_loc
            if neighbor not in frontier:
                frontier.appendleft(neighbor)

    return shortest_paths


def task(input_filepath, task_num=1):
    puzzle = input_filepath.read_text().split("\n")
    hmap, start_loc, end_loc = _read_height_map(puzzle)
    shortest_distances = bfs(hmap, end_loc)
    if task_num == 1:
        print(f"Part 1 solution: {shortest_distances[start_loc]}")
    else:
        print(f"Part 2 solution: {min(shortest_distances.values())}")
        print("Confucius says: Every problem is a search problem")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day12.txt"
    task(input_path, task_num=1)
    task(input_path, task_num=2)
