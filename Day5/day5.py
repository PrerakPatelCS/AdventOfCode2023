with open('Almanac.txt', 'r') as file:
    seeds = file.readline().split()[1:]
    seeds = [int(num) for num in seeds]
    data = []
    line = file.readline()
    while line:
        temp = []
        while line and line[0].isdigit():
            nums = line.split()
            nums = [int(num) for num in nums]
            temp.append(nums)
            line = file.readline()
        if temp:
            data.append(temp)

        line = file.readline()

seedToSoil = data[0]
soilToFertilizer = data[1]
fertilizerToWater = data[2]
waterToLight = data[3]
lightToTemp = data[4]
tempToHumidity = data[5]
humidityToLocation = data[6]

print(seedToSoil)
print(soilToFertilizer)
print(fertilizerToWater)
print(waterToLight)
print(lightToTemp)
print(tempToHumidity)
print(humidityToLocation)

# Destination range start, source range state, range length


def materialChange(materials:list, changeTo:list) -> list:
    # convert to each layer
    layer = []
    for mat in materials:
        change = mat
        for dest, source, range in changeTo:
            if source <= mat < source + range:
                change = dest + (mat - source)
        layer.append(change)

    print(layer)
    return layer

print(seeds)

def puzzle1() -> None:
    soil = materialChange(seeds, seedToSoil)
    fertilizer = materialChange(soil, soilToFertilizer)
    water = materialChange(fertilizer, fertilizerToWater)
    light = materialChange(water, waterToLight)
    temp = materialChange(light, lightToTemp)
    humidity = materialChange(temp, tempToHumidity)
    location = materialChange(humidity, humidityToLocation)
    print(min(location))


puzzle1()
# 165788812
