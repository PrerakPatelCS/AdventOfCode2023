import math

with open('Directions.txt', 'r') as file:
    dirs = file.readline().strip()
    file.readline()
    network = {}
    for line in file:
        data = line.split()
        network[data[0]] = {'L': data[2][1:4], 'R': data[3][:3]}


# Start at AAA and traverse until ZZZ
def puzzle1() -> None:
    location = 'AAA'
    steps = 0
    while not location == 'ZZZ':
        location = network[location][dirs[steps % len(dirs)]]
        steps += 1
    print(steps)


# Get all the distances to get the an ending of A to and ending of Z
# then find the LCM of those since it repeats
def puzzle2() -> None:
    locations = [location for location in network if location[2] == 'A']
    ans = []
    for location in locations:
        steps, cur = 0, location
        while not cur[2] == 'Z':
            cur = network[cur][dirs[steps % len(dirs)]]
            steps += 1
        ans.append(steps)
    print(math.lcm(*ans))


puzzle1()  # 15517
puzzle2()  # 14935034899483

