def puzzle1() -> None:
    # Open a file in read mode
    with open('Calibrations.txt', 'r') as file:
        # Read the file line by line
        sum = 0
        for line in file:
            line = puzzle2Helper(line)
            first, last = 0, 0
            for digit in line:
                if digit.isdigit():
                    if first == 0:
                        first = int(digit)
                    last = int(digit)
            number = first * 10 + last
            sum += number
    print(sum)


def puzzle2Helper(word: str) -> str:
    number_words = {
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine"
    }
    for key, value in number_words.items():
        word = word.replace(key, value)
    return word




if __name__ == "__main__":
    puzzle1()

# Get the first and last numbers make it a double digit number
# sum all calibrations
# puzzle 2 was convert a string "one" to a number 1
# Puzzle 1 = 55172
# Puzzle 2 = 54925
