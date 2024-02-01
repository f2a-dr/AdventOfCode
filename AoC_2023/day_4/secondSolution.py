# Advent of Code 2023
# Day 4: Scratchcards -- Part 2

filename = "puzzle_input.txt"

scratchcards = []
winsInCards = []

with open(filename) as f:
    for line in f:
        scratchcards.append(1)
        line = line.strip()
        line = line.split(':')[1]
        winningNumbers = line.split("|")[0].split()
        elfNumbers = line.split("|")[1].split()

        wins = 0
        for num in elfNumbers:
            if num in winningNumbers:
                wins += 1

        winsInCards.append(wins)


print(winsInCards)

for i in range(len(scratchcards)):
    addition = winsInCards[i]
    for j in range(i+1, addition+i+1):
        scratchcards[j] += scratchcards[i]

print("The total numbers of scratchcards is {}".format(sum(scratchcards)))
