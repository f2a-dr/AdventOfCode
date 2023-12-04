# Advent of Code 2023
# Day 3: Gear Ratios -- Part 1

def whereSymbols(string):
    positions = []
    for i in range(len(string)):
        if not(string[i].isalnum()) and string[i] != ".":
            positions.append(i)

    return positions
            
def whereNumbers(string):
    digits = []
    positions = []
    numbers = []
    locations = []
    for i in range(len(string)):
        if string[i].isnumeric():
            digits.append(string[i])
            positions.append(i)
        elif digits != []:
            numbers.append(int(''.join(digits)))
            locations.append(positions)
            digits = []
            positions = []
    
    if digits != []:
        numbers.append(int(''.join(digits)))
        locations.append(positions)
        digits = []
        positions = []

    return numbers, locations


filename = "puzzle_input.txt"

sum = 0
positionSpecial = []
valueNumbers = []
locationNumbers = []
lineCount = 0

with open(filename) as f:
    for line in f:
        line = line.strip()
        positionSpecial.append(whereSymbols(line))
        n, l = whereNumbers(line)
        for i in range(len(n)):
            valueNumbers.append(n[i])
            locationNumbers.append([lineCount, l[i]])
        lineCount += 1

for i in range(len(valueNumbers)):
    if locationNumbers[i][0] == 0:
        for j in range(len(positionSpecial[locationNumbers[i][0]])):
            if (locationNumbers[i][1][-1] + 1) >= positionSpecial[locationNumbers[i][0]][j] and (locationNumbers[i][1][0] - 1) <= positionSpecial[locationNumbers[i][0]][j]:
                sum += valueNumbers[i]
        for j in range(len(positionSpecial[locationNumbers[i][0]+1])):
            if (locationNumbers[i][1][-1] + 1) >= positionSpecial[locationNumbers[i][0]+1][j] and (locationNumbers[i][1][0] - 1) <= positionSpecial[locationNumbers[i][0]+1][j]:
                sum += valueNumbers[i]
    elif locationNumbers[i][0] == (lineCount - 1):
        for j in range(len(positionSpecial[locationNumbers[i][0]-1])):
            if (locationNumbers[i][1][-1] + 1) >= positionSpecial[locationNumbers[i][0]-1][j] and (locationNumbers[i][1][0] - 1) <= positionSpecial[locationNumbers[i][0]-1][j]:
                sum += valueNumbers[i]
        for j in range(len(positionSpecial[locationNumbers[i][0]])):
            if (locationNumbers[i][1][-1] + 1) >= positionSpecial[locationNumbers[i][0]][j] and (locationNumbers[i][1][0] - 1) <= positionSpecial[locationNumbers[i][0]][j]:
                sum += valueNumbers[i]
    else:
        for j in range(len(positionSpecial[locationNumbers[i][0]-1])):
            if (locationNumbers[i][1][-1] + 1) >= positionSpecial[locationNumbers[i][0]-1][j] and (locationNumbers[i][1][0] - 1) <= positionSpecial[locationNumbers[i][0]-1][j]:
                sum += valueNumbers[i]
        for j in range(len(positionSpecial[locationNumbers[i][0]])):
            if (locationNumbers[i][1][-1] + 1) >= positionSpecial[locationNumbers[i][0]][j] and (locationNumbers[i][1][0] - 1) <= positionSpecial[locationNumbers[i][0]][j]:
                sum += valueNumbers[i]
        for j in range(len(positionSpecial[locationNumbers[i][0]+1])):
            if (locationNumbers[i][1][-1] + 1) >= positionSpecial[locationNumbers[i][0]+1][j] and (locationNumbers[i][1][0] - 1) <= positionSpecial[locationNumbers[i][0]+1][j]:
                sum += valueNumbers[i]

print(sum)
