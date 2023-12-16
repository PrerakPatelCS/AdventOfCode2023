with open('Platform.txt', 'r') as file:
    platform = [list(line.strip()) for line in file]

'''
Do not need to make the new platform
for each column find the number of round rocks there are
from the north edge to the either the first cubic rock, #,
or the south edge
'''


def getNorthBeamLoad() -> None:
    n, m = len(platform), len(platform[0])
    totalLoad = 0
    for i in range(n):
        for j in range(m):
            totalLoad += m - i if platform[i][j] == 'O' else 0
    print(totalLoad)


def tiltNorth() -> None:
    n, m = len(platform), len(platform[0])
    # loop though columns
    for col in range(m):
        roundRocks = 0
        restSpot = n
        for row in range(n):
            roundRocks += 1 if platform[row][col] == 'O' else 0
            if platform[row][col] == '#' or row == n - 1:
                for i in range(m - restSpot, row + 1):
                    if platform[i][col] == '#':
                        continue
                    platform[i][col] = 'O' if roundRocks > 0 else '.'
                    roundRocks -= 1
                roundRocks = 0
                restSpot = m - row - 1


def tiltSouth() -> None:
    n, m = len(platform), len(platform[0])
    # Loop through columns in reverse
    for col in range(m):
        roundRocks = 0
        restSpot = n
        # Loop through rows in reverse
        for row in reversed(range(n)):
            roundRocks += 1 if platform[row][col] == 'O' else 0
            if platform[row][col] == '#' or row == 0:
                for i in reversed(range(row, restSpot)):
                    if platform[i][col] == '#':
                        continue
                    platform[i][col] = 'O' if roundRocks > 0 else '.'
                    roundRocks -= 1
                roundRocks = 0
                restSpot = row


def tiltWest() -> None:
    n, m = len(platform), len(platform[0])
    # Loop through columns in reverse
    for row in range(n):
        roundRocks = 0
        restSpot = 0
        for col in range(m):
            roundRocks += 1 if platform[row][col] == 'O' else 0
            if platform[row][col] == '#' or col == m - 1:
                for i in range(restSpot, col + 1):
                    if platform[row][i] == '#':
                        continue
                    platform[row][i] = 'O' if roundRocks > 0 else '.'
                    roundRocks -= 1
                roundRocks = 0
                restSpot = col


def tiltEast() -> None:
    n, m = len(platform), len(platform[0])
    # Loop through columns in reverse
    for row in range(n):
        roundRocks = 0
        restSpot = m
        for col in reversed(range(m)):
            roundRocks += 1 if platform[row][col] == 'O' else 0
            if platform[row][col] == '#' or col == 0:
                for i in reversed(range(col, restSpot)):
                    if platform[row][i] == '#':
                        continue
                    platform[row][i] = 'O' if roundRocks > 0 else '.'
                    roundRocks -= 1
                roundRocks = 0
                restSpot = col


def cycle(cycles: int) -> None:
    for i in range(cycles):
        tiltNorth()
        tiltWest()
        tiltSouth()
        tiltEast()


cycle(1000)
getNorthBeamLoad()

