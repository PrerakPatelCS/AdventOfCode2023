with open('image.txt', 'r') as file:
    image = [line.strip() for line in file]

n, m = len(image), len(image[0])

# make a prefix sum for how many empty rows there
prefixRow = [0] * (n + 1)
prefixCol = [0] * (m + 1)

# expand the universe
for i in range(n):
    row = image[i]
    prefixRow[i + 1] += prefixRow[i] + 1 if len(set(row)) == 1 and row[0] == '.' else prefixRow[i]


def transpose(matrix: []) -> []:
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed


# transpose the matrix
image = transpose(image)
for i in range(m):
    col = image[i]
    prefixCol[i + 1] += prefixCol[i] + 1 if len(set(col)) == 1 and col[0] == '.' else prefixCol[i]
image = transpose(transpose(transpose(image)))


galaxies = []
for i in range(n):
    for j in range(m):
        if image[i][j] == '#':
            galaxies.append((i, j))

# get the manhattan distance between each galaxy and add them up
totalManhattanDist = 0
# Part 1 set to 1 for Part 2 set to 1,000,000
EXPANSION = 1_000_000
for i in range(len(galaxies)):
    galaxy1 = galaxies[i]
    for j in range(i + 1, len(galaxies)):
        galaxy2 = galaxies[j]

        numExpandRows = 0
        if galaxy1[0] > galaxy2[0]:
            numExpandRows = prefixRow[galaxy1[0] + 1] - prefixRow[galaxy2[0]]
        else:
            numExpandRows = prefixRow[galaxy2[0] + 1] - prefixRow[galaxy1[0]]

        numExpandCols = 0
        if galaxy1[1] > galaxy2[1]:
            numExpandCols = prefixCol[galaxy1[1] + 1] - prefixCol[galaxy2[1]]
        else:
            numExpandCols = prefixCol[galaxy2[1] + 1] - prefixCol[galaxy1[1]]

        manhattanDist = abs(galaxy1[0] - galaxy2[0]) + numExpandRows * (EXPANSION - 1) + \
                        abs(galaxy1[1] - galaxy2[1]) + numExpandCols * (EXPANSION - 1)

        totalManhattanDist += manhattanDist
print(totalManhattanDist)
