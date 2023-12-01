# Solution to Advent of code 2022
# Day 4: Camp Cleanup

def parser(s:str):
	int1 = []
	int2 = []
	n1 = ""
	n2 = ""
	n2_flag = False
	for i in range(len(s)):
		if s[i] != "-" and s[i] != "," and n2_flag == False:
			n1 = n1 + str(s[i])
		elif s[i] == "-":
			n2_flag = True
		elif s[i] == ",":
			n2_flag = False
			int1.append(int(n1))
			int1.append(int(n2))
			n1 = ""
			n2 = ""
		elif s[i] != "-" and s[i] != "," and n2_flag == True:
			n2 = n2 + str(s[i])
		#print(n2_flag)
		#print(n1)
		#print(n2)

	int2.append(int(n1))
	int2.append(int(n2))

	return int1, int2
		


filename="puzzle_input.txt"
#filename="test_input.txt"
containing_count = 0
overlapping_count = 0

with open(filename) as f:
	for line in f:
		section_1,section_2 = parser(line.strip())
		#print(section_1)
		#print(section_2)
		if ( section_1[0] <= section_2[0] and section_1[1] >= section_2[1] ) or ( section_2[0] <= section_1[0] and section_2[1] >= section_1[1] ):
			containing_count = containing_count + 1
		if ( section_1[0] >= section_2[0] and section_1[0] <= section_2[1] ) or ( section_1[1] >= section_2[0] and section_1[1] <= section_2[1] )		\
			or ( section_1[0] <= section_2[0] and section_1[1] >= section_2[1] ) or ( section_2[0] <= section_1[0] and section_2[1] >= section_1[1] ):
			overlapping_count = overlapping_count + 1 

print("\n### Part one solution ###")
print("Containing pairs: {}".format(containing_count))

print("\n### Part two solution ###")
print("Overlapping pairs: {}\n".format(overlapping_count))
