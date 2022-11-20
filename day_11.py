f_name = 'input_11'

data = []
with open(f_name) as f:
    for line in f.readlines():
        data.append([int(char) for char in line.strip('\n')])

h = len(data)
w = len(data[0])

def flash(row, col, data, flash_q, flashed):
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < h and 0 <= j < w and not (row, col) == (i, j):
                incre(i, j, data, flash_q, flashed)

def incre(row, col, data, flash_q, flashed):
    if not (row, col) in flashed:
        if data[row][col] < 9:
            data[row][col] += 1
        else:
            data[row][col] = 0
            flash_q.append((row, col))
            flashed.add((row, col))

n_steps = 999
n_flashes = 0
total_flashes = 0
for t in range(1, n_steps + 1):
    flash_q = []
    flashed = set()
    for i, row in enumerate(data):
        for j, oct in enumerate(row):
            incre(i, j, data, flash_q, flashed)

    while flash_q:
        i, j = flash_q.pop()
        flash(i, j, data, flash_q, flashed)
        n_flashes += 1
    
    if n_flashes == 100:
        print("Part 2 answer:", t)
        break
    
    total_flashes += n_flashes
    if t == 100:
        print("Part 1 answer:", total_flashes)
    
    n_flashes = 0