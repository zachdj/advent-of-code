from pathlib import Path


def task1(input_filepath):
    """compute tic-tac-toe score"""
    outcome_score = {
        "AX": 3,
        "AY": 6,
        "AZ": 0,
        "BX": 0,
        "BY": 3,
        "BZ": 6,
        "CX": 6,
        "CY": 0,
        "CZ": 3,
    }
    selection_score = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    total_score = 0
    with open(input_filepath, "r") as infile:
        line = infile.readline()
        while line:
            opponent_move = line[0]
            my_move = line[2]
            total_score += (
                outcome_score[opponent_move + my_move] + selection_score[my_move]
            )
            line = infile.readline()

    print(f"Total score: {total_score}")
    print("Happy Friday!")


def task2(input_filepath):
    # maps opponents move and desired outcome to my move
    move_map = {
        "AX": "C",
        "AY": "A",
        "AZ": "B",
        "BX": "A",
        "BY": "B",
        "BZ": "C",
        "CX": "B",
        "CY": "C",
        "CZ": "A",
    }
    outcome_score = {
        "AA": 3,
        "AB": 6,
        "AC": 0,
        "BA": 0,
        "BB": 3,
        "BC": 6,
        "CA": 6,
        "CB": 0,
        "CC": 3,
    }
    selection_score = {
        "A": 1,
        "B": 2,
        "C": 3,
    }
    with open(input_filepath, "r") as infile:
        total_score = 0
        line = infile.readline()
        while line:
            opponent_move = line[0]
            desired_outcome = line[2]
            my_move = move_map[opponent_move + desired_outcome]
            total_score += (
                outcome_score[opponent_move + my_move] + selection_score[my_move]
            )

            line = infile.readline()

    print(f"Total score: {total_score}")
    print("tic tac TOTAL DOMINATION")


if __name__ == "__main__":
    project_dir = Path(__file__).parents[1]
    input_path = project_dir / "inputs" / "day2.txt"
    task1(input_path)
    task2(input_path)
