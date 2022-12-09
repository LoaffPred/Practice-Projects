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
    x = coords[:1]
    y = coords[1:]
    for pair in enumerate(letters):
        if x == pair[1]:
            x = pair[0]
            return int(y), x
    else:
        raise


class Ship:
    def __init__(self, length):
        self.length = length
        self.name = length
        self.lives = self.length
        self.coords = []

    def deploy_ship(self):
        while True:
            try:
                for _ in range(self.length):
                    input_coords = input(
                        f"Enter coordinates for ship length {self.length}: "
                    )
                    valid_coords = coords_to_index(input_coords)
                    self.coords.append((valid_coords))
                return True
            except:
                print("!!! Invalid Input !!!")


def main():
    print_board(get_board("red_board"))
    ship2 = Ship(2)
    ship2.deploy_ship()
    print(ship2.coords)


main()
