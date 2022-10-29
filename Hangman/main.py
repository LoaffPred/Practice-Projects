# fmt: off
final_hangman = [
    ["_", "_", "_", "_"],
    ["|", " ", " ", "|"],
    ["|", " ", " ", "0"],
    ["|", " ", "/", "|", "\\"],
    ["|", " ", "/", " ", "\\"],
    ["|"],
    ["=", "=", "=", "=", "=", "=", "=",],
]
# fmt: on

mistakes = {
    "1": ["0", "2,3"],
    "2": ["|", "3,3"],
    "3": ["/", "3,2"],
    "4": ["\\", "3,4"],
    "5": ["/", "4,2"],
    "6": ["\\", "4,4"],
}


def print_hangman(man):
    for row in man:
        for x in row:
            print(x, end="")
        print()


def format_word(word):
    blank_list = []
    word_list = []
    for l in word:
        word_list.append(l.upper())
        if l == " ":
            blank_list.append(" ")
        else:
            blank_list.append("_")
    return word_list, blank_list


def new_words():
    words = []
    input_words = input("Enter word/s to guess: ").upper().split(" ")
    for word in input_words:
        words.append(word)
    return words


# print(letter, sep=" ")
