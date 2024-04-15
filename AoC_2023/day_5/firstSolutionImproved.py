# Advent of Code 2023
# Day 5: If You Give A Seed A Fertilizer

def appender(counter, inputList, outputIndex):
    counter += 1
    while inputList[counter].strip() != "":
        toSave = inputList[counter].strip().split(" ")
        toSave = [int(_) for _ in toSave]
        toSource = [toSave[1], toSave[1]+toSave[2]-1]
        toDestination = [toSave[0], toSave[0]+toSave[2]-1]
        source[outputIndex].append(toSource)
        destination[outputIndex].append(toDestination)
        if counter == (len(inputList)-1):
            break
        counter += 1

filename = "puzzle_input.txt"

Nmaps = 7

source = [[] for _ in range(Nmaps)]
destination = [[] for _ in range(Nmaps)]
seeds = []
mapsPos = {
    "seed-to-soil": 0,
    "soil-to-fertilizer": 1,
    "fertilizer-to-water": 2,
    "water-to-light": 3,
    "light-to-temperature": 4,
    "temperature-to-humidity": 5,
    "humidity-to-location": 6
}

with open(filename) as f:
    lines = f.readlines()
    for _ in range(len(lines)):
        if lines[_].startswith("seeds:"):
            line = lines[_].strip().split(":")
            line = line[1].strip().split(" ")
            for __ in line:
                seeds.append(int(__))
        elif lines[_].strip().split(" ")[0] in mapsPos:
            outputIndex = mapsPos[lines[_].strip().split(" ")[0]]
            appender(_, lines,outputIndex)

locations = seeds.copy()
for _ in range(len(locations)):
    for __ in range(len(source)):
        for ___ in range(len(source[__])):
            if locations[_] >= source[__][___][0] and locations[_] <= source[__][___][1]:
                locations[_] = destination[__][___][0] + (locations[_] - source[__][___][0])
                break


print(seeds)
print(locations)
print(min(locations))
