from queue import Queue


with open('Contraption.txt', 'r') as file:
    contraption = [list(line.strip()) for line in file]
    # the \ appears as \\ but everything else is normal

"""
Traverse the contraption starting at 0,0 and pointing to 0, n
| and - splits the laser into 2 if you reach the flat side
We can simulate this with DFS 
We also want to make sure we do not go in an infinite loop
Not good enough to just mark a coord visited, we need the direction as well
If we are at the same coord and from the same direction we are done for that 
path
the total energized tiles can be found by the length of the set 
of all coords, without the directions
"""
def bfs(x: int, y: int, direction: tuple) -> int:
    n, m = len(contraption), len(contraption[0])
    coords = set()
    visited = set()
    q = Queue()
    q.put((x, y, direction))

    while not q.empty():
        currX, currY, currDirection = q.get()

        if 0 > currX or currX >= n or 0 > currY or currY >= m:
            continue
        coords.add((currX, currY))
        visited.add((currX, currY, currDirection))

        # change direction based on what is at x and y
        if contraption[currX][currY] == '.':
            newX, newY = currX + currDirection[0], currY + currDirection[1]
            if (newX, newY, currDirection) not in visited:
                q.put((newX, newY, currDirection))
        elif contraption[currX][currY] == '\\':
            newDirection = currDirection[::-1]
            newX, newY = currX + newDirection[0], currY + newDirection[1]
            if (newX, newY, newDirection) not in visited:
                q.put((newX, newY, newDirection))
        elif contraption[currX][currY] == '/':
            newDirection = tuple(num * -1 for num in currDirection)[::-1]
            newX, newY = currX + newDirection[0], currY + newDirection[1]
            if (newX, newY, newDirection) not in visited:
                q.put((newX, newY, newDirection))
        elif contraption[currX][currY] == '|':
            if currDirection[0] == 0:
                newDirection = (1, 0)
                newX, newY = currX + newDirection[0], currY + newDirection[1]
                if (newX, newY, newDirection) not in visited:
                    q.put((newX, newY, newDirection))
                newDirection = (-1, 0)
                newX, newY = currX + newDirection[0], currY + newDirection[1]
                if (newX, newY, newDirection) not in visited:
                    q.put((newX, newY, newDirection))
            else:
                newX, newY = currX + currDirection[0], currY + currDirection[1]
                if (newX, newY, currDirection) not in visited:
                    q.put((newX, newY, currDirection))
        elif contraption[currX][currY] == '-':
            if currDirection[1] == 0:
                newDirection = (0, 1)
                newX, newY = currX + newDirection[0], currY + newDirection[1]
                if (newX, newY, newDirection) not in visited:
                    q.put((newX, newY, newDirection))
                newDirection = (0, -1)
                newX, newY = currX + newDirection[0], currY + newDirection[1]
                if (newX, newY, newDirection) not in visited:
                    q.put((newX, newY, newDirection))
            else:
                newX, newY = currX + currDirection[0], currY + currDirection[1]
                if (newX, newY, currDirection) not in visited:
                    q.put((newX, newY, currDirection))
    return len(coords)


def puzzle(puzzleNum=1) -> None:
    n, m = len(contraption), len(contraption[0])

    if puzzle == 1:
        print(bfs(0, 0, (0, 1)))
    else:
        maxEnergy = 0

        for i in range(n):
            maxEnergy = max(maxEnergy, bfs(i, 0, (0, 1)), bfs(i, n - 1, (0, -1)))

        for i in range(m):
            maxEnergy = max(maxEnergy, bfs(0, i, (1, 0)), bfs(m - 1, i, (-1, 0)))

        print(maxEnergy)


puzzle(puzzleNum=2)  # between 7111 and 7999
