from functools import cmp_to_key
from numbers import Number
from pathlib import Path


def compare(packet1, packet2):
    """Recursively compare two packets"""
    if isinstance(packet1, Number) and isinstance(packet2, Number):
        # base case - two integers
        if packet1 == packet2:
            return 0
        elif packet1 < packet2:
            return -1
        else:
            return 1
    elif isinstance(packet1, Number) and isinstance(packet2, list):
        return compare([packet1], packet2)
    elif isinstance(packet1, list) and isinstance(packet2, Number):
        return compare(packet1, [packet2])
    else:
        # base case, empty list(s)
        if not packet1 and not packet2:
            return 0
        elif not packet1 and packet2:
            return -1
        elif packet1 and not packet2:
            return 1
        else:
            # recurse over shortened list
            elem1, elem2 = packet1[0], packet2[0]
            result = compare(elem1, elem2)
            if result == 0:
                return compare(packet1[1:], packet2[1:])
            return result


def task1(input_filepath):
    puzzle = input_filepath.read_text().split("\n")
    correct_order_indices = []
    pair_idx = 0
    for i in range(0, len(puzzle), 3):
        pair_idx += 1
        packet1 = eval(puzzle[i])
        packet2 = eval(puzzle[i + 1])
        if compare(packet1, packet2) == -1:
            correct_order_indices.append(pair_idx)

    print(f"Part 1 solution: {sum(correct_order_indices)}")
    print("Happy Hot Cocoa Day!")


def task2(input_filepath):
    puzzle = [line for line in input_filepath.read_text().split("\n") if line]
    packets = [eval(line) for line in puzzle]
    packets.extend([[[2]], [[6]]])
    sorted_packets = sorted(packets, key=cmp_to_key(compare))
    idx1, idx2 = sorted_packets.index([[2]]) + 1, sorted_packets.index([[6]]) + 1

    print(f"Part 2 solution: {idx1 * idx2}")
    print("Happy National Violin Day!")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day13.txt"
    task1(input_path)
    task2(input_path)
