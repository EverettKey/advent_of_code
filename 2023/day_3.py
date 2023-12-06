f_name = "input_3"

lines = None
with open(f_name) as f:
    lines = f.readlines()
    
searched = set()
stk = []
def get_n(i, j):
    while 0 <= j and lines[i][j].isdigit():
        j -= 1
    
    j += 1

    n = 0
    while lines[i][j].isdigit():
        n *= 10
        n += int(lines[i][j])
        searched.add((i,j))
        j += 1
    return n


part_1 = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line[:-1]):
        if not char.isdigit() and not char == '.':
            for r, c in [(i-1,j-1), (i, j-1), (i+1, j-1), (i-1,j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)]:
                if 0 <= r < len(lines) and 0<=c< len(line) and lines[r][c].isdigit() and not (r,c) in searched:
                    n = get_n(r,c)
                    print(n)
                    part_1 += n
print(part_1)

part_2 = 0
searched = set()
for i, line in enumerate(lines):
    for j, char in enumerate(line[:-1]):
        if char == '*':
            searched = set()
            ns = []
            for r, c in [(i-1,j-1), (i, j-1), (i+1, j-1), (i-1,j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)]:
                if 0 <= r < len(lines) and 0<=c< len(line) and lines[r][c].isdigit() and not (r,c) in searched:
                    ns.append(get_n(r,c))
            if len(ns) == 2:
                part_2 += ns[0] * ns[1]
print(part_2)
                    
                