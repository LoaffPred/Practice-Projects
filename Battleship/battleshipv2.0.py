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
    board[coords[0]][coords[1]] = data


def validate_coords(input_coords, board):
    try:
        row, col = coords_to_index(input_coords)
        if board[row][col] == " S ":
            print("!!! Space already occupied !!!")
            return False
        else:
            print("$$$ Valid coordinates $$$")
            return row, col
    except Exception as e:
        print(e)
        return False


class Ship:
    def __init__(self, length):
        self.length = length
        self.name = length
        self.lives = self.length
        self.coords = []

    def deploy_ship(self, board):
        for _ in range(self.length):
            while True:
                input_coords = input(
                    f"Enter coordinates for ship length {self.length}: "
                )
                valid_coords = validate_coords(input_coords, board)
                if valid_coords:
                    self.coords.append((valid_coords))
                    plot_on_board(" S ", valid_coords, board)
                    break


def main():
    red_board = get_board("red_board")
    print_board(red_board)
    ship2 = Ship(2)
    ship2.deploy_ship(red_board)
    print(ship2.coords)


main()
