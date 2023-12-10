# Advent of code 2023
# Day 3: Gear Ratios -- Part 2

def whereGears(string):
    positions = []
    for i in range(len(string)):
        if string[i] == "*":
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
positionGears = []
valueNumbers = []
locationNumbers = []
lineCount = 0

with open(filename) as f:
    for line in f:
        line = line.strip()
        positionGears.append(whereGears(line))
        n, l = whereNumbers(line)
        for i in range(len(n)):
            valueNumbers.append(n[i])
            locationNumbers.append([lineCount, l[i]])
        lineCount += 1


# For the '*' on the first line
if positionGears[0] != '':
    for i in range(len(positionGears[0])):
        gearRatio = []
        for j in range(len(locationNumbers)):
            if locationNumbers[j][0] == 0:
                if locationNumbers[j][1][-1] == (positionGears[0][i] - 1):
                    gearRatio.append(valueNumbers[j])
                elif locationNumbers[j][1][0] == (positionGears[0][i] + 1):
                    gearRatio.append(valueNumbers[j])
            elif locationNumbers[j][0] == 1:
                if positionGears[0][i] >= (locationNumbers[j][1][0] - 1) and positionGears[0][i] <= (locationNumbers[j][1][-1] + 1):
                    gearRatio.append(valueNumbers[j])
        print(len(gearRatio))
        if len(gearRatio) == 2:
            sum += gearRatio[0]*gearRatio[1]

# For the '*' on the line from the second to the last second
for k in range(1, len(positionGears) - 1):
    if positionGears[k] != '':
        for i in range(len(positionGears[k])):
            gearRatio = []
            for j in range(len(locationNumbers)):
                if locationNumbers[j][0] == (k - 1):
                    if positionGears[k][i] >= (locationNumbers[j][1][0] - 1) and positionGears[k][i] <= (locationNumbers[j][1][-1] + 1):
                        gearRatio.append(valueNumbers[j])
                elif locationNumbers[j][0] == k:
                    if locationNumbers[j][1][-1] == (positionGears[k][i] - 1):
                        gearRatio.append(valueNumbers[j])
                    elif locationNumbers[j][1][0] == (positionGears[k][i] + 1):
                        gearRatio.append(valueNumbers[j])
                elif locationNumbers[j][0] == (k + 1):
                    if positionGears[k][i] >= (locationNumbers[j][1][0] - 1) and positionGears[k][i] <= (locationNumbers[j][1][-1] + 1):
                        gearRatio.append(valueNumbers[j])
            if len(gearRatio) == 2:
                sum += gearRatio[0]*gearRatio[1]

# For the '*' on the last line
if positionGears[-1] != '':
    for i in range(len(positionGears[-1])):
        gearRatio = []
        for j in range(len(locationNumbers)):
            if locationNumbers[j][0] == 0:
                if locationNumbers[j][1][-1] == (positionGears[-1][i] - 1):
                    gearRatio.append(valueNumbers[j])
                elif locationNumbers[j][1][0] == (positionGears[-1][i] + 1):
                    gearRatio.append(valueNumbers[j])
            elif locationNumbers[j][0] == len(positionGears) - 2:
                if positionGears[-1][i] >= (locationNumbers[j][1][0] - 1) and positionGears[-1][i] <= (locationNumbers[j][1][-1] + 1):
                    gearRatio.append(valueNumbers[j])
        if len(gearRatio) == 2:
            sum += gearRatio[0]*gearRatio[1]

            
print(sum)
