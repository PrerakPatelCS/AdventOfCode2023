with open('ValueHistories.txt', 'r') as file:
    valuesHistory = []
    for line in file:
        valuesHistory.append(list(map(int, line.split())))


def puzzle1() -> None:
    sumValues = 0
    for values in valuesHistory:
        curr = values
        extrapolate = values[-1]
        while any(curr):
            curr = [curr[i + 1] - curr[i] for i in range(len(curr) - 1)]
            extrapolate += curr[-1]
        sumValues += extrapolate
    print(sumValues)


def puzzle2() -> None:
    sumValues = 0
    for values in valuesHistory:
        curr = values
        extrapolate = values[0]
        count = 0
        while any(curr):
            curr = [curr[i + 1] - curr[i] for i in range(len(curr) - 1)]
            extrapolate += curr[0] if count % 2 == 1 else -curr[0]
            count += 1
        sumValues += extrapolate
    print(sumValues)


puzzle1()  # 2174807968
puzzle2()  # 1208
