import math
import time
f_name = "input_12"


start = [-1,-1]
end = [-1,-1]
heights = []
with open(f_name) as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        horz_line = []
        for j, char in enumerate(line.strip('\n')):
            if char == 'S':
                start = [i,j]
                char = 'a'
            elif char == 'E':
                end = [i, j]
                char = 'z'
            horz_line.append(ord(char) - ord('a'))
        heights.append(horz_line)

def print_searched():
    grid = ''
    for i in range(h):
        line = ''
        for j in range(w):
            if (i, j) in [tuple(start), tuple(end)]:
                line += '%'
            elif (i, j) in searched:
                line += lines[i][j]
                
            else:
                line += '_'
        grid += line
        grid += '\n'
    print(grid)
    time.sleep(0.025)

print(start, end)
h = len(heights)
w = len(heights[0])
# steps = [[math.inf for i in range(w)] for j in range(h)]
# print(steps)
q = [(tuple(start), 0)]
searched = set(tuple(start))
answer1 = 0
while q:
    row_col, n_steps = q.pop(0)
    r, c = row_col

    if [r, c] == end:
        answer1 = n_steps
        break

    for row, col in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
        coord = (row, col)
        if 0 <= row < h and 0 <= col < w and coord not in searched:
            if heights[row][col] - heights[r][c] < 2:
                q.append((coord, n_steps+1))
                searched.add(coord)
    
    print_searched()
    # print(searched)

        


q = [(tuple(end), 0)]
searched = set(tuple(end))
answer2 = 0
while q:
    row_col, n_steps = q.pop(0)
    r, c = row_col

    if lines[r][c] == 'a':
        answer2 = n_steps
        break

    for row, col in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
        coord = (row, col)
        if 0 <= row < h and 0 <= col < w and coord not in searched:
            if heights[r][c] - heights[row][col] < 2:
                q.append((coord, n_steps+1))
                searched.add(coord)
    
    print_searched()
    # print(searched)
print(answer1)
print(answer2)
