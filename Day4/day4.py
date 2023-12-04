# open file
with open('Cards.txt', 'r') as file:
    cards = [line.strip() for line in file]


ELFCARDS = 10
total = 0
numberOfWins = list()


# Part 1
for card in cards:
    # get rid of the "Card  ###:"
    card = card.split(':')[1]
    nums = card.split(' ')
    count = 0
    elf, myCards = set(), set()
    for num in nums:
        if not num.isdigit():
            continue

        if count < ELFCARDS:
            elf.add(int(num))
        else:
            myCards.add(int(num))
        count += 1
    wins = len(myCards.intersection(elf))
    total += 2 ** (wins - 1) if wins > 0 else 0
    numberOfWins.append(wins)

print(total)

# part 2

totalCards = 0
numberOfCards = [1 for i in range(len(numberOfWins))]

for i in range(len(numberOfWins)):
    for j in range(i + 1, i + numberOfWins[i] + 1):
        numberOfCards[j] += numberOfCards[i]

print(sum(numberOfCards))

# Puzzle 1 22488
# Puzzle 2 7013204
