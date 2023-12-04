with open('Cards.txt', 'r') as file:
    cards = [line.strip() for line in file]

# part 1

ELFCARDS = 10
total = 0

numberOfWins = list()

for card in cards:
    # get rid of the "Card  ###:"
    card = card.split(':')[1]
    nums = card.split(' ')
    count = 0
    elf, myCards = list(), list()
    for num in nums:
        if not num.isdigit():
            continue

        if count < ELFCARDS:
            elf.append(int(num))
        else:
            myCards.append(int(num))
        count += 1
    wins = 0
    for win in elf:
        if win in myCards:
            wins += 1
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
