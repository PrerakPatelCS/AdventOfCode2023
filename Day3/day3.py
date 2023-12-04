import string

with open('Schematics.txt', 'r') as file:
    matrix = file.read().strip().split('\n')

n = len(matrix)
m = len(matrix[0])

numberLocations = {}


def getNumberLocations() -> None:
    start, end = 0, 0
    sum = 0
    for i in range(n):
        j = 0
        while j < m:
            if matrix[i][j].isdigit():
                locations = set()
                num = 0
                start = j
                while j < m and matrix[i][j].isdigit():
                    locations.add((i, j))
                    num *= 10
                    num += int(matrix[i][j])
                    j += 1
                end = j - 1
                if numNearSymbol(i, start, end):
                    sum += num
                for location in locations:
                    numberLocations[location] = num
            j += 1

    print(sum)
    #print(numberLocations)

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


def surroundingNumbers(row: int, col: int) -> int:
    #print("NUMBERS")
    dirs = [1, 0, -1, 0, 1, 1, -1, -1, 1]
    nums = set()
    for i in range(0, len(dirs) - 1):
        newX, newY = row + dirs[i], col + dirs[i + 1]
        if newX < 0 or newX >= n or newY < 0 or newY >= m:
            continue
        if matrix[newX][newY].isdigit():
            nums.add(numberLocations[(newX, newY)])
            #print(newX, newY)

    if len(nums) < 2:
        return 0
    product = 1
    print(row, col)
    print()
    for num in nums:
        print(num)
        product *= num
    print()
    return product


def getGearLocations() -> None:
    sumRatios = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '*':
                #print(i, j)
                sumRatios += surroundingNumbers(i, j)
    print(sumRatios)


if __name__ == "__main__":
    getNumberLocations()
    getGearLocations()

# Puzzle 1 531932
# Puzzle 2 73646890