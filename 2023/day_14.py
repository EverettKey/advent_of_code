f_name = "input_14"

lines = []
with open(f_name) as f:
	f_lines = f.readlines()
	for line in f_lines:
		lines.append(line.strip('\n'))

part_1 = 0
h = len(lines)
w = len(lines[0])

stops = [0] * w
spaces = [['.'] * w for i in range(h)]
for i in range(h):
	for j in range(w):
		print((i,j))
		if lines[i][j] == "#":
			stops[j] = i + 1
			spaces[i][j] = '#'
		elif lines[i][j] == "O":
			spaces[stops[j]][j] = 'O'
			part_1 += h - stops[j]
			stops[j] += 1
for i in range(h):
	print(''.join(spaces[i]))

print("Part_1:", part_1)
print(h, w)

def slide(board, dir):
	if dir[0] == 0:
		
	else:
		stops = [0] * h
	new_board = [['.'] * w for i in ra
	for i in range(h):	
