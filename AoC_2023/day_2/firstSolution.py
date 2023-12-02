# Advent of Code 2023
# Day 2: Cube Conundrum -- Part 1

maxCubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

filename = "puzzle_input.txt"
result = 0

with open(filename) as f:
    for line in f:
        impossible = False
        line = line.strip()
        line = line.split(":")
        game = line[0].split()[1]
        line = line[1].split(";")
        for i in range(len(line)):
            draw = line[i]
            draw = draw.split(",")
            for j in range(len(draw)):
                cubes = draw[j]
                cubes = cubes.split()
                if int(cubes[0]) > maxCubes[cubes[1]]:
                    print("Game " + game + " is impossible! :(")
                    impossible = True
                    break
        if not(impossible):
            result += int(game)

print(result)

