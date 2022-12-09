import json


def get_board(board_name):
    # file directory might change
    with open(f"Battleship\\{board_name}.json", "r") as f:
        return json.load(f)


def write_board(data, board_name):
    with open(f"Battleship\\{board_name}.json", "w") as f:
        json.dump(data, f)


def print_board(board):
    for row in board:
        for col in row:
            print(col, end="|")
        print()


def main():
    print_board(get_board("red_board"))


main()
