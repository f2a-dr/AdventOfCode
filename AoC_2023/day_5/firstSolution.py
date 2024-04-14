# Advent of Code 2023
# Day 5: If You Give A Seed A Fertilizer

import numpy as np

filename = "puzzle_input.txt"

def appender(counter, inputList, outputList):
    counter += 1
    while inputList[counter].strip() != "":
        toSave = inputList[counter].strip().split(" ")
        outputList.append([int(x) for x in toSave])
        if counter == (len(inputList)-1):
            break
        counter += 1

def mapper(inputList):
    highMax = 600000000

    outputList = np.linspace(0, highMax, highMax+1, dtype=int)
    # print(outputList)
    for _ in range(len(inputList)):
        newVal = inputList[_][0]
        for __ in range(inputList[_][1], inputList[_][1]+inputList[_][2]):
            outputList[__] = int(newVal)
            newVal += 1

    return outputList



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


seedToSoilMap = mapper(seedToSoil)
soilToFertilizerMap = mapper(soilToFertilizer)
fertilizerToWaterMap = mapper(fertilizerToWater)
waterToLightMap = mapper(waterToLight)
lightToTemperatureMap = mapper(lightToTemperature)
temperatureToHumidityMap = mapper(temperatureToHumidity)
humidityToLocationMap = mapper(humidityToLocation)


# print(seedToSoilMap)
# print(soilToFertilizerMap)
# print(fertilizerToWaterMap)
# print(waterToLightMap)
# print(lightToTemperatureMap)
# print(temperatureToHumidityMap)
# print(humidityToLocationMap)

location = []
for _ in seeds:
    location.append(humidityToLocationMap[temperatureToHumidityMap[lightToTemperatureMap[waterToLightMap[fertilizerToWaterMap[soilToFertilizerMap[seedToSoilMap[_]]]]]]])
print(min(location))
