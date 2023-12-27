from queue import Queue

with open('Garden.txt', 'r') as file:
    garden = [list(line.strip()) for line in file]

start = ()
n, m = len(garden), len(garden[0])
for i in range(n):
    for j in range(m):
        if garden[i][j] == 'S':
            start = (i, j)

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def puzzle1() -> int:
    steps = 1000
    q = Queue()
    q.put(start)
    count = 0
    while not q.empty() and steps > 0:
        size = q.qsize()
        plots = set()
        for _ in range(size):
            node = q.get()
            for dir in dirs:
                newX, newY = node[0] + dir[0], node[1] + dir[1]
                if 0 <= newX < n and 0 <= newY < m and garden[newX][newY] != '#'\
                        and not (newX, newY) in plots:
                    plots.add((newX, newY))
                    q.put((newX, newY))
        steps -= 1
        count = len(plots)
        print(count)
    return count


print(puzzle1())

