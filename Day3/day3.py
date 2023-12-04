import string

with open('Schematics.txt', 'r') as file:
    matrix = file.read().strip().split('\n')

n = len(matrix)
m = len(matrix[0])


def getNumberLocations() -> None:
    start, end = 0, 0
    sum = 0
    for i in range(n):
        j = 0
        while j < m:
            if matrix[i][j].isdigit():
                num = 0
                start = j
                while j < m and matrix[i][j].isdigit():
                    num *= 10
                    num += int(matrix[i][j])
                    j += 1
                end = j - 1
                if numNearSymbol(i, start, end):
                    sum += num
            j += 1
    print(sum)


# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
def isSymbol(symbol: str) -> bool:
    return symbol != '.' and symbol in string.punctuation


def numNearSymbol(row:int, colStart:int, colEnd:int) -> bool:
    # check all around the number for symbols
    # check above and below
    for j in range(colStart, colEnd + 1):
        if row - 1 >= 0 and isSymbol(matrix[row - 1][j]):
            return True
        if row + 1 < n and isSymbol(matrix[row + 1][j]):
            return True
    # check left
    if colStart - 1 >= 0:
        # up 1 middle and down 1
        if row + 1 < n and isSymbol(matrix[row + 1][colStart - 1]):
            return True
        if isSymbol(matrix[row][colStart - 1]):
            return True
        if row - 1 >= 0 and isSymbol(matrix[row - 1][colStart - 1]):
            return True

    # check right
    # check left
    if colEnd + 1 < m:
        # up 1 middle and down 1
        if row + 1 < n and isSymbol(matrix[row + 1][colEnd + 1]):
            return True
        if isSymbol(matrix[row][colEnd + 1]):
            return True
        if row - 1 >= 0 and isSymbol(matrix[row - 1][colEnd + 1]):
            return True

    return False


def getGearLocations() -> None:
    sum = 0
    for i in range(n):
        j = 0
        while j < m:
            if matrix[i][j] == '*':
                print(i, j)
            j += 1


if __name__ == "__main__":
    getNumberLocations()
    getGearLocations()
