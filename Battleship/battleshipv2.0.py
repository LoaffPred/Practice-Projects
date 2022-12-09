import json

# file directory might change
with open("Battleship\\red_board.json", "r") as f:
    board = json.load(f)


for row in board:
    for col in row:
        print(col, end="")
    print()
