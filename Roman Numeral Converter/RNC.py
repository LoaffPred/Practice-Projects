input_num = input("Enter a number to convert [0-10,000]: ")


class LetterEquivalent:
    def __init__(self, base, half, next_):
        self.base = base
        self.half = half
        self.next_ = next_
        self.letters = {"base": self.base, "half": self.half, "next": self.next_}

    def letter(self, value):
        if value == "1":
            rn = self.base * 1
        elif value == "2":
            rn = self.base * 2
        elif value == "3":
            rn = self.base * 3
        elif value == "4":
            rn = self.base + self.half
        elif value == "5":
            rn = self.half
        elif value == "6":
            rn = self.half + self.base * 1
        elif value == "7":
            rn = self.half + self.base * 2
        elif value == "8":
            rn = self.half + self.base * 3
        elif value == "9":
            rn = self.base + self.next_
        else:
            rn = ""

        return rn


ones = LetterEquivalent("I", "V", "X")
tens = LetterEquivalent("X", "L", "C")
hundreds = LetterEquivalent("C", "D", "M")
thousands = LetterEquivalent("M", "v-", "x-")  # temp values for 5000 and 10000


def convert(num):
    num_str = ""
    if len(num) == 1:
        num_str += ones.letter(num[0])
    elif len(num) == 2:
        num_str += tens.letter(num[0])
        num_str += ones.letter(num[1])
    elif len(num) == 3:
        num_str += hundreds.letter(num[0])
        num_str += tens.letter(num[1])
        num_str += ones.letter(num[2])
    elif len(num) == 4:
        num_str += thousands.letter(num[0])
        num_str += hundreds.letter(num[1])
        num_str += tens.letter(num[2])
        num_str += ones.letter(num[3])

    return num_str


print(convert(input_num))
