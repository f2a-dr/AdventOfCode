# Advent of Code 2023
# Day 4: Scratchcards -- Part 1

filename = "puzzle_input.txt"

points = 0

with open(filename) as f:
    for line in f:
        line = line.strip()
        line = line.split(':')[1]
        winningNumbers = line.split("|")[0].split()
        elfNumbers = line.split("|")[1].split()


        wins = 0
        for num in elfNumbers:
            if num in winningNumbers:
                # print("{} is winning".format(num))
                wins += 1

        if wins > 0:
            points += 2**(wins - 1)

print(points)
        


