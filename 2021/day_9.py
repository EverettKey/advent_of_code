f_name = "input_9"

data = []
with open(f_name) as f:
    lines = f.readlines()
    for line in lines:
        data_line = [int(num) for num in line.strip('\n')]
        data.append(data_line)
h = len(data)
w = len(data[0])

def is_low_point(i, j ,data):
    for a, b in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
        if 0 <= a < h and 0 <= b < w:
            if data[a][b] <= data[i][j]:
                return False
    return True


ans1 = 0
for i, row in enumerate(data):
    for j, num in enumerate(row):
        if is_low_point(i, j, data):
            ans1 += num + 1

print("Part 1 answer:", ans1)

'''
Part 2
'''

data2 = data.copy()

def bfs(starting_point, data):
    q = [starting_point]
    touched = set()
    count = 0
    while q:
        count += 1
        i, j = q.pop(0)
        data[i][j] = 9

        for row, col in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            if (row, col) not in touched and \
               0 <= row < h and 0 <= col < w and \
               not data[row][col] == 9:
                q.append((row, col))
                touched.add((row, col))

    return count

basins = []
for i, row in enumerate(data2):
    for j, col in enumerate(row):
        if not data2[i][j] == 9:
            basins.append(bfs((i, j), data2))
            basins.sort()
            if len(basins) > 3:
                basins.pop(0)

basins.sort()
ans2 = basins[-1] * basins[-2] * basins[-3]
print("Part 2 answer", ans2)
        

    
