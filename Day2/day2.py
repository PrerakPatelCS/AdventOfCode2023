import re


def puzzle1() -> None:
    # Open a file in read mode
    with open('Games.txt', 'r') as file:
        # Read the file line by line
        sum, red, green, blue = 0, 12, 13, 14
        for line in file:
            possible = True
            # raw string
            data = re.split(r'[:,;]', line)
            game = int(re.split(r'[ ]', data[0])[1])
            for i in range(1, len(data)):
                if len(data[i]) == 1:
                    continue
                round = re.split(r'[ ]', data[i].strip())
                marbles = int(round[0])
                color = round[1]
                if color == 'red' and marbles > red:
                    possible = False
                    break
                elif color == 'blue' and marbles > blue:
                    possible = False
                    break
                elif color == 'green' and marbles > green:
                    possible = False
                    break
                print(round)
            if possible:
                sum += game
                #print(game, sum, line)

    print(sum)


def puzzle2() -> None:
    # Open a file in read mode
    with open('Games.txt', 'r') as file:
        # Read the file line by line
        sum = 0
        for line in file:
            # raw string
            data = re.split(r'[:,;]', line)
            game = int(re.split(r'[ ]', data[0])[1])
            red, green, blue = 1, 1, 1
            for i in range(1, len(data)):
                if len(data[i]) == 1:
                    continue
                round = re.split(r'[ ]', data[i].strip())
                marbles = int(round[0])
                color = round[1]
                if color == 'red':
                    red = max(red, marbles)
                elif color == 'blue':
                    blue = max(blue, marbles)
                elif color == 'green':
                    green = max(green, marbles)

            power = red * blue * green
            sum += power
            #print(game, sum, line)

    print(sum)


if __name__ == "__main__":
    puzzle2()

# puzzle 1 2317
# puzzle 2 74804