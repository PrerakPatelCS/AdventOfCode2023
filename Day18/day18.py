with open('DigPlan.txt', 'r') as file:
    digPlan = [tuple(line.strip().split()) for line in file]

dirs = {
    'R': complex(0, 1),
    'L': complex(0, -1),
    'D': complex(1, 0),
    'U': complex(-1, 0)
}
getDir = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}


def shoelace(vertices: list[complex]) -> float:
    area = 0
    n = len(vertices)
    for i in range(n - 1):
        area += vertices[i].real * vertices[i + 1].imag
    area += vertices[n - 1].real * vertices[0].imag

    for i in range(n - 1):
        area -= vertices[i + 1].real * vertices[i].imag
    area -= vertices[0].real * vertices[n - 1].imag

    return abs(area) / 2


'''
Using Shoelace + pick's theorem
'''
def getTotalSpace(directions: list, distances: list[int]) -> int:
    curIndex = complex(0, 0)
    vertices = [curIndex]
    circumference = 0
    for dir, num in zip(directions, distances):
        num = int(num)
        newCoord = curIndex + dirs[dir] * num
        vertices.append(newCoord)
        curIndex = newCoord
        circumference += num
    vertices.append(complex(0, 0))
    area = shoelace(vertices)
    print(circumference, area)
    return circumference / 2 + area + 1


def puzzle1() -> int:
    directions = [x[0] for x in digPlan]
    distances = [x[1] for x in digPlan]
    return getTotalSpace(directions, distances)


def puzzle2() -> int:
    directions = []
    distances = []
    for _, _, color in digPlan:
        distances.append(int(color[2: 7], 16))
        directions.append(getDir[color[-2]])
    return getTotalSpace(directions, distances)


print(puzzle1())  # 35991
print(puzzle2())  #
