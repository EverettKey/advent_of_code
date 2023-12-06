f_name = "input_8"

field = []
with open(f_name) as f:
    lines = f.readlines()
    for line in lines:
        row = [int(tree) for tree in line.strip('\n')]
        field.append(row)

h = len(field)
w = len(field[0])

seen_trees = set()

def look_in(i, j, field):
    if   i == 0  : row_mod, col_mod  = (1, 0)
    elif i == h-1: row_mod, col_mod  = (-1, 0)
    elif j == 0  : row_mod, col_mod  = (0, 1)
    elif j == w-1: row_mod, col_mod  = (0, -1)

    row, col = i, j
    tallest_tree = -1
    while 0 <= row < h and 0 <= col < w:# and \
         # (row, col) not in seen_trees:
        print(i, j, row, col)
        if tallest_tree < field[row][col]:
            seen_trees.add((row, col))
            tallest_tree = field[row][col]
        row += row_mod
        col += col_mod

def walk_around(field):
    for i in range(h):
        look_in(i,   0, field)
        look_in(i, w-1, field)
    for j in range(w):
        look_in(0,   j, field)
        look_in(h-1, j, field)
def print_seen():
    for i in range(h):
        for j in range(w):
            if (i, j) in (seen_trees):
                print('X', end="")
            else: print(' ', end="")    
        print()

walk_around(field)
print_seen()

print("Part 1 answer:", len(seen_trees))
print(h, w)


h_marks = [[-1] for i in range(w)]
w_marks = [[-1] for i in range(h)]