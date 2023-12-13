from queue import Queue

with open('Tiles.txt', 'r') as file:
    tiles = [line for line in file]

n, m = len(tiles), len(tiles[0])
# get pipe loop
pipeLoop = []
# find S the starting point
for i in range(n - 1):
    for j in range(m - 1):
        if tiles[i][j] == 'S':
            pipeLoop.append((i, j))
            break

print(pipeLoop)

directions = {'north': (-1, 0), 'east': (0, 1), 'south': (1, 0), 'west': (0, -1)}

# the direction is the way you want to move
'''
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal

Each pipe makes you go in one direction
enter one way come out the other
We consider the direction you are traveling to get to the pipe and then 
the direction it makes you travel
|
Travel North exit North
Travel South exit South
-
Travel East exit East
Travel West exit West
L
Travel South exit East
Travel West exit North
J
Travel South exit West
Travel East exit North
7
Travel North exit West
Travel East exit South
F
Travel North exit East
Travel West exit South
.
no pipe
S
start can go any direction
DFS take in a direction traveling 
'''
visited = set()
x, y = pipeLoop[0][0], pipeLoop[0][1]
direction = 'north'
while not (pipeLoop[0][0], pipeLoop[0][1]) in visited:
    newX = x + directions[direction][0]
    newY = y + directions[direction][1]
    if 0 <= newX < n and 0 <= newY < m and (newX, newY) not in visited:
        c = tiles[newX][newY]
        visited.add((newX, newY))
        if direction == 'north':
            if c == '|':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'north'
            elif c == '7':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'west'
            elif c == 'F':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'east'
        elif direction == 'west':
            if c == '-':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'west'
            elif c == 'L':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'north'
            elif c == 'F':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'south'
        elif direction == 'east':
            if c == '-':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'east'
            elif c == '7':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'south'
            elif c == 'J':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'north'
        elif direction == 'south':
            if c == '|':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'south'
            elif c == 'L':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'east'
            elif c == 'J':
                pipeLoop.append((newX, newY))
                x, y, direction = newX, newY, 'west'
        # print(c, newX, newY)

# part 1
# print(pipeLoop, len(pipeLoop), len(pipeLoop) / 2)
# 6757
pipeLoop = visited  # dynamic typing

# part 2  find all tiles inside the loop
outsideLoop = set()
print((0, 0) in pipeLoop)
# (0,0) not in loop start there and do BFS to get every node node in the loop
start = (0, 0)
nodes = Queue()
nodes.put((0, 0))
outsideLoop.add((0, 0))
while not nodes.empty():
    node = nodes.get()
    for direction in directions:
        newX = node[0] + directions[direction][0]
        newY = node[1] + directions[direction][1]
        if 0 <= newX < n and 0 <= newY < m and \
                (newX, newY) not in outsideLoop and \
                (newX, newY) not in pipeLoop:
            nodes.put((newX, newY))
            outsideLoop.add((newX, newY))

# print(outsideLoop)
print((n * m) - len(outsideLoop) - len(pipeLoop))

# get all spots not obviously outside
for i in range(n - 1):
    for j in range(m - 1):
        if (i, j) not in outsideLoop and (i, j) not in pipeLoop:
            print((i, j))
