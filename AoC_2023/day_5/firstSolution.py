# Advent of Code 2023
# Day 5: If You Give A Seed A Fertilizer

filename = "test_input.txt"

def appender(counter, inputList, outputList):
    counter += 1
    while inputList[counter].strip() != "":
        toSave = inputList[counter].strip().split(" ")
        outputList.append([int(x) for x in toSave])
        if counter == (len(inputList)-1):
            break
        counter += 1

seeds = []
seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

with open(filename) as f:
    lines = f.readlines()
    for _ in range(len(lines)):
        if lines[_].startswith("seeds:"):
            print(lines[_])
            line = lines[_].strip().split(":")
            line = line[1].strip().split(" ")
            for __ in range(len(line)):
                seeds.append(int(line[__]))
        elif lines[_].startswith("seed-to-soil"):
            appender(_, lines, seedToSoil)
        elif lines[_].startswith("soil-to-fertilizer"):
            appender(_, lines, soilToFertilizer)
        elif lines[_].startswith("fertilizer-to-water"):
            appender(_, lines, fertilizerToWater)
        elif lines[_].startswith("water-to-light"):
            appender(_, lines, waterToLight)
        elif lines[_].startswith("light-to-temperature"):
            appender(_, lines, lightToTemperature)
        elif lines[_].startswith("temperature-to-humidity"):
            appender(_, lines, temperatureToHumidity)
        elif lines[_].startswith("humidity-to-location"):
            appender(_, lines, humidityToLocation)


print(seeds)
print(seedToSoil)
print(soilToFertilizer)
print(fertilizerToWater)
print(waterToLight)
print(lightToTemperature)
print(temperatureToHumidity)
print(humidityToLocation)
