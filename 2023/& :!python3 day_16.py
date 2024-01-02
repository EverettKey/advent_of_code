f_name = "input_16_t"
lines = []
with open(f_name) as f:
	lines = f.readlines()
q = [(0,0,0,1)] # (r, c, r_mod, c_mod)
visited = set(q)

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
mirror_map = {'.':[], '/': [cw90], '\\': [ccw90], '-': [cc90, cw90], '|':[cc90, cw90]}

part_1 = 1
for r, c, dir_r, dir_c in q:
	char = lines[r][c]
	for operation in mirror_map[char]:
	r_mod, c_mod = operation((r_mod, c_mod))
	new_r, new c= r + r_mod, c + c_mod
	if (new_r, new_c) not in visited:
		if 0 <= new_r < h and 0 <= new_c < w:
			part_1 += 1
			q.append((new_r, new_c, r_mod, c_mod))
			visited.add((new_r, new_c))
			
print("Part_1", part_1NAME
