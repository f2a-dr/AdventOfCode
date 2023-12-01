# Solution to Advent of code 2022
# Day 2: Rock Paper Scissors

points_1 = 0
points_2 = 0
win = 6
draw = 3
loss = 0
rock = 1
paper = 2
scissors = 3

with open("puzzle_input.txt") as f:
	for line in f:
		line.strip()
		line.split()
		if line[0] == "A":
			if line[2] == "X":
				points_1 = points_1 + rock + draw
			elif line[2] == "Y":
				points_1 = points_1 + paper + win
			elif line[2] == "Z":
				points_1 = points_1 + scissors + loss
		elif line[0] == "B":
			if line[2] == "X":
				points_1 = points_1 + rock + loss
			elif line[2] == "Y":
				points_1 = points_1 + paper + draw
			elif line[2] == "Z":
				points_1 = points_1 + scissors + win
		elif line[0] == "C":
			if line[2] == "X":
				points_1 = points_1 + rock + win
			elif line[2] == "Y":
				points_1 = points_1 + paper + loss
			elif line[2] == "Z":
				points_1 = points_1 + scissors + draw


with open("puzzle_input.txt") as f:
	for line in f:
		line.strip()
		line.split()
		if line[0] == "A":
			if line[2] == "X":
				points_2 = points_2 + loss + scissors
			elif line[2] == "Y":
				points_2 = points_2 + draw + rock
			elif line[2] == "Z":
				points_2 = points_2 + win + paper
		elif line[0] == "B":
			if line[2] == "X":
				points_2 = points_2 + loss + rock
			elif line[2] == "Y":
				points_2 = points_2 + draw + paper
			elif line[2] == "Z":
				points_2 = points_2 + win + scissors
		elif line[0] == "C":
			if line[2] == "X":
				points_2 = points_2 + loss + paper
			elif line[2] == "Y":
				points_2 = points_2 + draw + scissors
			elif line[2] == "Z":
				points_2 = points_2 + win + rock


print("\n### Part one solution ###")
print("Total points: {}".format(points_1))

print("\n### Part two solution ###")
print("Total points: {}\n".format(points_2))
