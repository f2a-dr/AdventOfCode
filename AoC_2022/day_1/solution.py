# Solution to Advent of code 2022
# Day 1: Calories Counting

elf_calories = []

with open("puzzle_input.txt") as f:
	calories = 0
	for line in f:
		if line.strip() == "":
			elf_calories.append(calories)
			calories = 0
		else:
			calories = calories + int(line.strip())

elf_calories.sort()

print("\n### Part one solution ###")
print("Total calories: {}".format(elf_calories[-1]))

print("\n### Part two solution ###")
print("Total calories: {}\n".format(elf_calories[-1]+elf_calories[-2]+elf_calories[-3]))
