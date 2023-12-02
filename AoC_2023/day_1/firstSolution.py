# Advent of Code 2023
# Day 1: Trebuchet?! -- Part 1

strings = []
numbers = []
sum = 0

with open("puzzle_input.txt") as f:
    for line in f:
        strings.append(line.strip())


for i in range(len(strings)):
    for j in strings[i]:
        try:
            int(j)
            numbers.append(int(j))
        except ValueError:
            pass

    if len(numbers) == 1:
        sum += numbers[0]
        sum += numbers[0]*10
    else:
        sum += numbers[-1]
        sum += numbers[0]*10

    numbers = []

print(sum)
