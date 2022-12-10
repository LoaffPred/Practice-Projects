import json


def get_board(board_name):
    # file directory might change
    with open(f"Battleship\\Boards\\{board_name}.json", "r") as f:
        return json.load(f)


def write_board(data, board_name):
    with open(f"Battleship\\Boards\\{board_name}.json", "w") as f:
        json.dump(data, f)


def print_board(board):
    for row in board:
        for col in row:
            print(col, end="|")
        print()


def coords_to_index(coords):
    letters = ["X", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    col = coords[:1]
    row = coords[1:]
    for pair in enumerate(letters):
        if col == pair[1]:
            col = pair[0]
            return int(row), col
    else:
        raise Exception("Coordinates Out of Bounds")


def plot_on_board(data, coords, board):
    row, col = coords
    board[row][col] = data


def validate_coords(input_coords, board):
    row, col = coords_to_index(input_coords)
    if board[row][col] == " S ":
        return False
    else:
        return row, col


class Ship:
    def __init__(self, length):
        self.length = length
        self.name = length
        self.lives = self.length
        self.coords = []

    def deploy_ship(self, board):
        while True:
            # try:
            for _ in range(self.length):
                input_coords = input(
                    f"Enter coordinates for ship length {self.length}: "
                )
                valid_coords = validate_coords(input_coords, board)
                if valid_coords:
                    self.coords.append((valid_coords))
                    plot_on_board(valid_coords, " S ", board)
                else:
                    print("TEST")
                    raise Exception("!!! Invalid Coordinates !!!")
            return True
        # except Exception:
        #     print("!!! Invalid Input !!!")


def main():
    red_board = get_board("red_board")
    print_board(red_board)
    ship2 = Ship(2)
    ship2.deploy_ship(red_board)
    print(ship2.coords)


main()
