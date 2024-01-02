
f_name = "input_10_t"

'''
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west. (1, 1)
F is a 90-degree bend connecting south and east. (, 1)
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.'''


pipe_lookup = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
    '.': [(0, 0), (0,0 )],
    'S': [(-1, 0), (1, 0), (0, 1), (0, -1)],
}

lines = []
start_coord = (0,0)
with open(f_name) as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i] = lines[i].strip('\n')
        for j, char in enumerate (lines[i]):
            if lines[i][j] == 'S':
                start_coord = (i,j)

def get_connections(coord):
    r, c = coord
    pipe_char = lines[r][c]
    connections = []
    for r_mod, c_mod in pipe_lookup[pipe_char]:
        connect_r, connect_c = r + r_mod, c + c_mod
        if 0 <= connect_r < h and 0 <= connect_c < w:
            connections.append((connect_r, connect_c))
    return connections

h = len(lines)
w = len(lines[0])
print(start_coord)
r, c = start_coord
pipe_set = set()
pipe_list = []
start_connections = get_connections(start_coord)
for neigh_coord in start_connections:
    for back_r, back_c in get_connections(neigh_coord):
        if (back_r, back_c) == start_coord:
            pipe_list.append(neigh_coord)
            pipe_set.add(neigh_coord)


def trace_pipe(coord):
    char = lines[coord]

while pipe_list:
    pipe_coord = pipe_list.pop()
    for connection in get_connections(pipe_coord):
        if connection not in pipe_set:
            pipe_list.append(connection)
            pipe_set.add(connection)
print(len(pipe_set), pipe_set)

part_1 = len(pipe_set) // 2
print("Part_1:", part_1)
# test: 8

def count_crossings(start_coord, dir):
    r_mod, c_mod = dir
    r, c = start_coord
    n_crossing = 0
    while 0 <= r < h and 0 <= c < w:
        pipe_char = lines[r][c]
        if pipe_char in '|-' and (r, c) in pipe_set and dir not in pipe_lookup[pipe_char]:
            n_crossing += 1
        r += dir[0]
        c += dir[1]
    return n_crossing

def is_inside(coord):
    dirs = pipe_lookup['S']
    for dir in dirs:
        print(dirs)
        n_crossings = count_crossings(coord, dir)
        if n_crossings % 2 == 0:
            return False
    return True


n_inside = 0
for i in range(h):
    for j in range(w):
        if is_inside((i,j)):
            n_inside += 1

part_2 = n_inside
print("Part_2:", part_2)