# Solution to Advent of code 2022
# Day 7: No Space Left On Device

filename = "test_input.txt"

lines = []
directories = []
fileSizes = []
files = []

with open(filename) as f:
    for line in f:
        lines.append(line)
        if line.strip().split()[1] == "cd" and line.strip().split()[2] != "..":
            directories.append(line.strip().split()[2])
        if line.strip().split()[0].isnumeric():
            fileSizes.append(line.strip().split()[0])
            files.append(line.strip().split()[1])

for i in range(len(directories)):
    for j in range(len(lines)):
        if lines[j] == "$ cd " + directories[i]:
            k = j



print(directories)
print(files)
print(fileSizes)
print(lines)
