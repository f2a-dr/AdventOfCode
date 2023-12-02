# Advent of Code 2023
# Day 2: Cube Conundrum -- Part 2

filename="puzzle_input.txt"

games = []
powers = []

with open(filename) as f:
    for line in f:
        line = line.strip()
        line = line.split(":")[1]
        line = line.split(";")
        for i in range(len(line)):
            line[i] = line[i].split(",")
            for j in range(len(line[i])):
                line[i][j] = line[i][j].split()
        games.append(line)
        # print(line)
# print(games)

for i in range(len(games)):
    minRed = 0
    minGreen = 0
    minBlue = 0
    for j in range(len(games[i])):
        for k in range(len(games[i][j])):
            if games[i][j][k][1] == "red" and int(games[i][j][k][0]) > minRed:
                minRed = int(games[i][j][k][0])
            elif games[i][j][k][1] == "green" and int(games[i][j][k][0]) > minGreen:
                minGreen = int(games[i][j][k][0])
            elif games[i][j][k][1] == "blue" and int(games[i][j][k][0]) > minBlue:
                minBlue = int(games[i][j][k][0])
    powers.append(minRed*minGreen*minBlue)

print(powers)
print(sum(powers))
