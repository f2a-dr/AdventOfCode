# Solution to Advent of code 2022
# Day 6: Tuning Trouble


filename = "puzzle_input.txt"
#filename = "test_input.txt"

with open(filename) as f:
	for line in f:
		line = line.strip()
		signal = line

signal_marker = 4
message_marker = 14


signal_found = False
j = 0
while not signal_found:
	signal_found = True
	chunk = signal[j:j+signal_marker]
	for k in range(len(chunk)):
		check_chunk = chunk[:k] + chunk[k+1:]
		if chunk[k] in check_chunk:
			signal_found=False
			break
	signal_pos = j + signal_marker
	j = j+1

message_found = False
j = 0
while not message_found:
	message_found = True
	chunk = signal[j:j+message_marker]
	for k in range(len(chunk)):
		check_chunk = chunk[:k] + chunk[k+1:]
		if chunk[k] in check_chunk:
			message_found=False
			break
	message_pos = j + message_marker
	j = j+1

	

print("\n### Part one solution ###")
print("Characters to signal: {}".format(signal_pos))

print("\n### Part two solution ###")
print("Characters to message: {}\n".format(message_pos))

