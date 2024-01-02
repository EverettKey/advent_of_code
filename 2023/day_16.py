f_name = "input_16_t"
lines = []
with open(f_name) as f:
	lines = f.readlines()
q = [(0,0,0,1)] # (r, c, r_mod, c_mod)
visited = set([(0,0)])
simulated = set(q)

def ccw90(dir):
	y, x = dir
	x = -x
	x, y = y, x
	return (y, x)

def cw90(dir): 
	y, x = dir  # (1, 0) (-1, 0)
	y, x = x, y # (0, 1) (0, -1)
	x = -x      # (0, -1) (0, 1)
	return (y, x) # (0, -1) 

def straight(dir):
	return dir

mirror_map = {'.':[straight], '/': [cw90], '\\': [ccw90], '-': [ccw90, cw90], '|':[ccw90, cw90]}

h = len(lines)
w = len(lines[0])
part_1 = 1
for r, c, dir_r, dir_c in q:
	char = lines[r][c]
	if char == '-' and dir_r == 0:
		char = '.'
	if char == '|' and dir_c == 0:
		char = '.'
	for operation in mirror_map[char]:
		print(r, c, char, operation)
		r_mod, c_mod = operation((dir_r, dir_c))
		new_r, new_c = r + r_mod, c + c_mod
		if (new_r, new_c, r_mod, c_mod) not in simulated:
			if 0 <= new_r < h and 0 <= new_c < w:
				part_1 += 1
				q.append((new_r, new_c, r_mod, c_mod))
				simulated.add((new_r, new_c, r_mod, c_mod))
				visited.add((new_r, new_c))

for i in range(h):
	line = ''
	for j in range(w):
		if (i, j) in visited:
			line = line + '#'
		else:
			line = line + '.'
	print(line)
print(ccw90((0,1)))
print(cw90((0,1)))
			
print("Part_1", part_1)
