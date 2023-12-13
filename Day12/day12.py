with open('Records.txt', 'r') as file:
    records = []
    for line in file:
        data = line.strip().split()
        data[1] = list(map(int, data[1].split(',')))
        records.append(data)


def puzzle1() -> None:
    totalNumWays = 0

    def backtrack(gears: str, index: int) -> int:
        if index == len(gears):
            return 1
        for i in range(index, len(gears)):
            if gears[i] == '?':
                period = gears[:i] + '.' + gears[i + 1:]
                backtrack(period, i + 1)
                hashtag = gears[:i] + '#' + gears[i + 1:]
                backtrack(hashtag, i + 1)
        return 0

    for record in records:
        springs = record[0]
        groups = record[1]
        numWays = backtrack(springs, 0)
        print(springs, groups)
        totalNumWays += numWays
    print(totalNumWays)


puzzle1()
print(records)
