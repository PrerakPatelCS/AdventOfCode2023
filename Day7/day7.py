from collections import Counter
from functools import cmp_to_key

with open('Cards.txt', 'r') as file:
    cards = []
    for line in file:
        data = line.split()
        cards.append((data[0], int(data[1])))

cardValue = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1,  # 11 for puzzle 1, 1 for puzzle 2
    'Q': 12,
    'K': 13,
    'A': 14
}


# Create a value of the hand and make sure you have duplicate hits
def getRating(card: tuple) -> int:
    freq = Counter(card[0])
    rating = 0
    for val, count in freq.items():
        rating += count * count
    return rating


# Puzzle 2
def getJokerRating(hand: tuple) -> int:
    freq = Counter(hand[2])
    rating = 0
    for val, count in freq.items():
        rating += count * count
    return rating


def getHandValue(hand1: tuple, hand2: tuple, joker=True) -> int:
    rating1, rating2 = getRating(hand1), getRating(hand2)
    if joker:
        rating1, rating2 = getJokerRating(hand1), getJokerRating(hand2)
    if rating1 == rating2:
        values1 = [cardValue[card] for card in hand1[0]]
        values2 = [cardValue[card] for card in hand2[0]]
        if values1 > values2:
            return 1
        else:
            return -1

    return rating1 - rating2


def puzzle1(hands: list) -> None:
    hands = sorted(hands, key=cmp_to_key(getHandValue))
    rank, totalWinnings = 1, 0
    for hand in hands:
        print(hand)
        totalWinnings += hand[1] * rank
        rank += 1
    print(totalWinnings)


def puzzle2(hands: list) -> None:
    jokerHands = []
    for hand in hands:
        if 'J' not in hand[0]:
            jokerHands.append((hand[0], hand[1], hand[0]))
            continue
        if hand[0] == 'JJJJJ':
            jokerHands.append((hand[0], hand[1], 'AAAAA'))
            continue
        freq = Counter(hand[0])
        high, highValue, highCount = '2', 0, 0
        for val, count in freq.items():
            if val == 'J':
                continue
            if highCount < count:
                highCount = count
                high = val
                highValue = cardValue[val]
            elif highValue < cardValue[val] and highCount == count:
                high = val
                highValue = cardValue[val]
        newHand = ''
        for card in hand[0]:
            newHand += high if card == 'J' else card
        jokerHands.append((hand[0], hand[1], newHand))

    puzzle1(jokerHands)


# puzzle1(cards)  # 248113761
puzzle2(cards)  # 246285222
