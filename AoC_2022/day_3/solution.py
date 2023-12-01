# Solution to Advent of code 2022
# Day 3: Rucksack Reorganization


def priority_converter(c:str):
	alphabeth = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(len(alphabeth)):
		if alphabeth[i] == c:
			return i+1

def compare_compartments(c1:str, c2:str):
	for i in range(len(c1)):
		for j in range(len(c2)):
			if c1[i] == c2[j]:
				return c1[i]

def compare_groups(r1:str, r2:str, r3:str):
	commons = []
	for i in range(len(r1)):
		for j in range(len(r2)):
			if r1[i] == r2[j]:
				commons.append(r1[i])
	for k in range(len(commons)):
		for l in range(len(r3)):
			if commons[k] == r3[l]:
				return commons[k]

#filename="test_input.txt"
filename="puzzle_input.txt"
rucksack = []
priority_single = 0
priority_groups = 0


with open(filename) as f:
	for line in f:
		line = line.strip()
		rucksack.append(line)

for i in range(len(rucksack)):
	compartment_1 = rucksack[i][0:int(len(rucksack[i])/2)]
	compartment_2 = rucksack[i][int(len(rucksack[i])/2)::]
	c = compare_compartments(compartment_1, compartment_2)
	priority_single = priority_single + priority_converter(c)

for j in range(0,len(rucksack),3):
	b = compare_groups(rucksack[j], rucksack[j+1], rucksack[j+2])
	priority_groups = priority_groups + priority_converter(b)



print("\n### Part one solution ###")
print("Total priority: {}".format(priority_single))

print("\n### Part two solution ###")
print("Total groups priority: {}\n".format(priority_groups))
