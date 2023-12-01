# Solution to Advent of code 2022
# Day 5: Supply Stack

import copy

def reader(input_file:str):
	initial_pos = []
	moves_n = []
	starting_p = []
	ending_p = []
	nrows = -1
	with open(input_file) as f:
		for line in f:
			line = line.split()
			nrows = nrows + 1
			if line[0] == "1":
				ncolumns = line[-1]
				break

	with open(input_file) as f:
		for i in range(nrows):
			line = next(f)
			row = []
			for j in range(1,len(line),4):
				row.append(line[j])
			initial_pos.append(row)
		next(f)
		next(f)
		for line in f:
			line = line.strip()
			line = line.split()
			moves_n.append(line[1])
			starting_p.append(line[3])
			ending_p.append(line[5])

	return moves_n, starting_p, ending_p, initial_pos

def crane(moves:int, start:int, end:int, state:list):
	for i in range(moves):
		state[end].append(state[start][-1])
		state[start].pop()
	
	return state

def crane9001(moves:int, start:int, end:int, state:list):
	moves = -1*moves
	for x in state[start][moves:]:
		state[end].append(x)
	del state[start][moves:]
	
	return state

filename = "puzzle_input.txt"
#filename = "test_input.txt"

moves_n, start_from, end_to, crates = reader(filename)
crates = [[row[i] for row in crates] for i in range(len(crates[0]))]
for row in crates:
	row.reverse() 

for i in range(len(crates)):
	while crates[i][-1] == ' ':
		crates[i].pop()

crates9001 = copy.deepcopy(crates)

for i in range(len(moves_n)):
	crates = crane(int(moves_n[i]), int(start_from[i])-1, int(end_to[i])-1, crates)
top_crates = ""
for i in range(len(crates)):
	top_crates = top_crates + crates[i][-1]


for i in range(len(moves_n)):
	crates9001 = crane9001(int(moves_n[i]), int(start_from[i])-1, int(end_to[i])-1, crates9001)
top_crates9001= ""
for i in range(len(crates9001)):
	top_crates9001 = top_crates9001 + crates9001[i][-1]



print("\n### Part one solution ###")
print("Top crates: {}".format(top_crates))

print("\n### Part two solution ###")
print("Top crates: {}\n".format(top_crates9001))
