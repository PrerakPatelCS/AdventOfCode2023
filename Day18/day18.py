from queue import Queue

with open('DigPlan.txt', 'r') as file:
    digPlan = [line.strip().split() for line in file]


dirs = {
    'R': (0, 1),
    'L': (0, -1),
    'D': (1, 0),
    'U': (-1, 0)
}
n = 100
digMap = [[0 for _ in range(n)] for _ in range(n)]
index = [1, 1]


def puzzle1() -> int:
    for dig in digPlan:
        dir = dirs[dig[0]]
        num = int(dig[1])
        color = dig[2]
        for i in range(num):
            digMap[index[0]][index[1]] = 1
            index[0] += dir[0]
            index[1] += dir[1]
    fillMap((1, 1))
    total = 0
    for x in digMap:
        for y in x:
            total += y
    return total


def fillMap(coord: tuple) -> None:
    nodes = Queue()
    nodes.put(coord)
    digMap[coord[0]][coord[1]] = 1
    while not nodes.empty():
        node = nodes.get()
        for h in dirs:
            dir = dirs[h]
            newX = node[0] + dir[0]
            newY = node[1] + dir[1]
            if 0 <= newX < n and 0 <= newY < n and digMap[newX][newY] != 1:
                nodes.put((newX, newY))
                digMap[newX][newY] = 1


print(puzzle1())  # 21115 too low
# 967357 too high
#  32643 too low
