with open('Frames.txt', 'r') as file:
    frames = []
    frame = []
    for line in file:
        line = line.strip()
        if len(line) == 0:
            frames.append(frame)
            frame = []
        else:
            frame.append(line)
    frames.append(frame)


# find reflection index and return that
# it will be the number of rows to the left
def puzzle1(strings: list[str], smudgesTarget: int = 0) -> int:
    n = len(strings)
    for split in range(n - 1):
        smudges = 0
        for i in range(n):
            if split + i + 1 >= n or split - i < 0 or smudges > smudgesTarget:
                break
            rowAbove = strings[split - i]
            rowBelow = strings[split + i + 1]
            for a, b in zip(rowAbove, rowBelow):
                smudges += 1 if a != b else 0
        if smudges == smudgesTarget:
            return split + 1
    return 0


def transpose(matrix: []) -> []:
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    transposed = list(map(''.join, transposed))
    return transposed


# Part 1 is 0 smudges and part 2 is 1 smudges
notes = 0
for panel in frames:
    transposedPanel = transpose(panel)
    notes += puzzle1(panel, 1) * 100 + puzzle1(transposedPanel, 1)
print(notes)
#  puzzle1() 33735
#  puzzle2() between 33735 and 39704
