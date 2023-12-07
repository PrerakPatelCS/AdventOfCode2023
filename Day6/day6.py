with open('TimesAndDistances.txt', 'r') as file:
    # returns an iterator
    times = map(int, file.readline().split()[1:])
    distances = map(int, file.readline().split()[1:])


# find all possible ways to beat the record and multiply them together
def puzzle1() -> None:
    product = 1
    for totalTime, recordDistance in zip(times, distances):
        recordBeating = 0
        for time in range(totalTime):
            distance = time * (totalTime - time)
            if distance > recordDistance:
                recordBeating += 1
        product *= recordBeating if recordBeating > 0 else 1
    print(product)


def puzzle2() -> None:
    totalTime = 44899691
    recordDistance = 277113618901768
    recordBeating = 0
    for time in range(totalTime):
        distance = time * (totalTime - time)
        if distance > recordDistance:
            recordBeating += 1
    print(recordBeating)


puzzle1()  # 2344708
#puzzle2()  # 30125202 this is costly
