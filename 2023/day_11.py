f_name = 'input_11'



lines = []
with open(f_name) as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    lines[i] = lines[i].strip('\n')

print(lines)
h = len(lines)
w = len(lines[0])
count_rows = [0] * h
count_cols = [0] * w
for i in range(h):
    for j in range(w):
        if lines[i][j] == '#':
            count_rows[i] += 1
            count_cols[j] += 1

print(count_rows)
print(count_cols)
empty_count = 0
expand_row = []
for i, count in enumerate(count_rows):
    if count_rows[i] == 0:
        empty_count += 1
    expand_row.append(empty_count)

empty_count = 0
expand_col = []
for i, count in enumerate(count_cols):
    if count_cols[i] == 0:
        empty_count += 1
    expand_col.append(empty_count)

print(expand_row)
print(expand_col)

coords = []
for i in range(h):
    for j in range(w):
        if lines[i][j] == '#':
            print(i, j, expand_row[i], expand_row[j])
            coords.append((i+expand_row[i], j+expand_col[j]))

print(coords)
part_1 = 0
n_stars = len(coords)
for i in range(n_stars):
    x1, y1 = coords[i]
    for j in range(i+1, n_stars):
        x2, y2 = coords[j]

        d = abs(x2-x1) + abs(y2 - y1)
        print(i, j ,coords[i], coords[j], d)
        part_1 += d
print("Part 1:", part_1)


coords = []
y = 1000000 - 1
# y = 10 - 1
for i in range(h):
    for j in range(w):
        if lines[i][j] == '#':
            print(i, j, expand_row[i], expand_row[j])
            coords.append((i+expand_row[i]*y, j+expand_col[j]*y))


print(coords)
part_2 = 0
n_stars = len(coords)
for i in range(n_stars):
    x1, y1 = coords[i]
    for j in range(i+1, n_stars):
        x2, y2 = coords[j]

        d = abs(x2-x1) + abs(y2 - y1)
        print(i, j ,coords[i], coords[j], d)
        part_2 += d
print("Part 2:", part_2)
# too high 544723977692