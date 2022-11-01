# fmt: off
final_board = [
    ["_", "_", "_", "_"],
    ["|", " ", " ", "|"],
    ["|", " ", " ", "0"],
    ["|", " ", "/", "|", "\\"],
    ["|", " ", "/", " ", "\\"],
    ["|"],
    ["=", "=", "=", "=", "=", "=", "=",],
]

new_board = [
    ["_", "_", "_", "_"],
    ["|", " ", " ", "|"],
    ["|", " ", " ", " "],
    ["|", " ", " ", " ", " "],
    ["|", " ", " ", " ", " "],
    ["|"],
    ["=", "=", "=", "=", "=", "=", "=",],
]
# fmt: on

mistakes = {
    "1": ["0", 2, 3],
    "2": ["|", 3, 3],
    "3": ["/", 3, 2],
    "4": ["\\", 3, 4],
    "5": ["/", 4, 2],
    "6": ["\\", 4, 4],
}


def print_board(board):
    for row in board:
        for x in row:
            print(x, end="")
        print()


def new_words():  # returns a list
    blank_letters = []
    new_letters = []
    input_words = input("Enter word/s to guess: ").upper().split()
    for word in input_words:
        for letter in word:
            new_letters.append(letter)  # no spaces
            blank_letters.append("_")
        blank_letters.append(" ")  # adds spaces between each word
    return new_letters, blank_letters


def get_guess():
    while True:
        guess = input("Enter your guess: ").upper()
        if len(guess) == 1:
            return guess
        else:
            print("Enter one letter only.")
        break


def get_mistake(number):
    new_board[mistakes[number][1]][mistakes[number][2]] = mistakes[number][0]


def print_letters(list):
    for letter in list:
        print(letter + " ", end="")
    print()


def main():
    mistake_counter = 0
    user_guesses = []
    new_letters, blank_letters = new_words()
    while True:
        print_board(new_board)

        print_letters(blank_letters)

        guess = get_guess()
        if guess in new_letters:
            if guess in user_guesses:
                pass
            else:
                guess_index = new_letters.index(guess)
                blank_letters[guess_index] = guess
                user_guesses.append(guess)
                if blank_letters == new_letters:
                    print("YOU WIN!")
                    break
        elif guess in user_guesses:
            print("Try again.")
            continue
        else:
            user_guesses.append(guess)
            mistake_counter += 1

        if mistake_counter == 1:
            get_mistake("1")
        elif mistake_counter == 2:
            get_mistake("2")
        elif mistake_counter == 3:
            get_mistake("3")
        elif mistake_counter == 4:
            get_mistake("4")
        elif mistake_counter == 5:
            get_mistake("5")
        elif mistake_counter == 6:
            get_mistake("6")
        elif mistake_counter == 7:
            print_board(new_board)
            print("You Lose...")
            break

        print("Used letters: ")
        print_letters(user_guesses)

        print(blank_letters)
        print(new_letters)


main()


# disallow repeating letters
# win message
# guess word


# awdadadadada
