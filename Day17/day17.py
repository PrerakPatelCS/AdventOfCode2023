from queue import PriorityQueue

with open('test3.txt', 'r') as file:
    heatMap = [list(map(int, line.strip())) for line in file]
n, m = len(heatMap), len(heatMap[0])

# Modified Dijkstra's
def puzzle1() -> int:
    pq = PriorityQueue()
    visited = set()
    # Amount Heat so far, Number of blocks in a row, coordinates
    # want the previous direction so we do not repeat
    # also it tells us which way is straight and not to repeat that way
    # 3 times in a row
    pq.put((0, 0, (0, 0), (0, 0), [(0, 0)]))
    visited.add((0, 0, (0, 0), (0, 0)))
    dirs = {(0, 1), (1, 0), (0, -1), (-1, 0)}
    while not pq.empty():
        heat, numBlocks, coord, direction, path = pq.get()
        # print(heat, numBlocks, coord, direction)
        # go left, right, and straight if numBlocks < 3
        if coord == (n - 1, m - 1):
            print(path)
            return heat
        prev = tuple(num * -1 for num in direction)
        for dir in dirs:
            # from the previous way
            if dir == prev:
                continue
            newX, newY = coord[0] + dir[0], coord[1] + dir[1]
            if newX < 0 or newX >= n or newY < 0 or newY >= m:
                continue
            newHeat = heat + heatMap[newX][newY]
            newNumBlocks = numBlocks + 1 if dir == direction else 1
            newCoord = (newX, newY)
            newPath = []
            for x in path:
                newPath.append(x)

            if newNumBlocks > 3:
                continue

            if (newHeat, newNumBlocks, newCoord, dir) not in visited:
                #  print(newHeat, newNumBlocks, newCoord, dir)
                visited.add((newHeat, newNumBlocks, newCoord, dir))
                newPath.append(newCoord)
                pq.put((newHeat, newNumBlocks, newCoord, dir, newPath))
        # print('__________________________________')


print(puzzle1())  # should be > 540 and < 645
# Got 638 but it was the solution to someone else's solution ???
# not 640
# ans is 635???
"""
This is too slow, too many states in visited so it repeats a lot of places
This is however the most accurate passes all testcases
"""

