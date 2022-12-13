from collections import defaultdict, deque
from heapq import heappop, heappush
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


def a_star(hmap, start_loc, end_loc, heuristic):
    """A* search from end to start, filtering illegal moves"""
    g_score = defaultdict(lambda: float("inf"))
    g_score[end_loc] = 0

    f_score = defaultdict(lambda: float("inf"))
    f_score[end_loc] = heuristic[end_loc]

    frontier = []
    heappush(frontier, (f_score[end_loc], end_loc))

    came_from = {}  # map from node to previous node in optimal path

    while frontier:
        current_f_score, current_loc = heappop(frontier)
        if current_loc == start_loc:
            # get path length
            path_len = 0
            while current_loc in came_from:
                current_loc = came_from[current_loc]
                path_len += 1
            return path_len

        row, col = current_loc
        current_height = hmap[current_loc]
        potential_neighbors = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
        ]
        legal_moves = [
            (r, c)
            for r, c in potential_neighbors
            if (r, c) in hmap and current_height - hmap[(r, c)] <= 1
        ]
        for neighbor in legal_moves:
            neighbor_g_score = g_score[current_loc] + 1
            if neighbor_g_score < g_score[neighbor]:
                came_from[neighbor] = current_loc
                g_score[neighbor] = neighbor_g_score
                f_score[neighbor] = neighbor_g_score + heuristic[neighbor]
                if neighbor not in frontier:
                    heappush(frontier, (f_score[neighbor], neighbor))

    # no path found
    return float("inf")


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


def task1(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    hmap, start_loc, end_loc = _read_height_map(puzzle)
    heuristic = {  # manhattan distance from current_loc to start
        (row, col): abs(row - start_loc[0]) + abs(col - start_loc[1])
        for row, col in hmap
    }
    shortest_path_len = a_star(hmap, start_loc, end_loc, heuristic)
    print(f"Part 1 solution: {shortest_path_len}")
    print("Santa loves A* !")


def task2(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    hmap, start_loc, end_loc = _read_height_map(puzzle)
    shortest_paths = bfs(hmap, end_loc)
    shortest_distances = [
        path_len for cell, path_len in shortest_paths.items() if hmap[cell] == 0
    ]

    print(f"Part 2 solution: {min(shortest_distances)}")
    print("Confucius says: Every problem is a search problem")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day12.txt"
    task1(input_path)
    task2(input_path)
