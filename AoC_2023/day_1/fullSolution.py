# Advent of Code 2023
# Day 1: Trebuchet?! -- Part 2

# strings = [ "two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

def numberSearcher(string):
    numbers = []
    positions = []
    spelledWithLetters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for n in range(len(spelledWithLetters)):
        index = 0
        while index < len(string):
            index = string.find(spelledWithLetters[n], index)
            if index == -1:
                break
            numbers.append(n+1)
            positions.append(index)
            index += len(spelledWithLetters[n])

    for i in range(len(string)):
        if string[i].isnumeric():
            numbers.append(int(string[i]))
            positions.append(i)

    return numbers, positions

sum = 0
strings = []

with open("puzzle_input.txt") as f:
    for line in f:
        strings.append(line.strip())

for line in strings:
    numberList, positionList = numberSearcher(line)
    # print(numberList)
    # print(positionList)
    # print(numberList[positionList.index(min(positionList))]*10+numberList[positionList.index(max(positionList))])
    sum += numberList[positionList.index(max(positionList))]
    sum += numberList[positionList.index(min(positionList))]*10


print(sum)
    






