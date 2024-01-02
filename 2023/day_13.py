
# 405
# n col to left + 100 * m rows above

f_name = 'input_13'



lines = []
with open(f_name) as f:
    lines = f.readlines()

fields = []
field = []
for line in lines:
    line = line.strip('\n')
    if len(line) == 0:
        fields.append(field)
        field = []
    else:
        row = []
        for cell in line:
            if cell == '.':
                row.append(0)
            else:
                row.append(1)
        field.append(row)
fields.append(field)

def encode_row(field, r):
    code = 0
    for cell in field[r]:
        code *= 2
        code += cell
    return code

def encode_col(field, c):
    code = 0
    for i in range(len(field)):
        code *= 2
        code += field[i][c]
    return code
for field in fields:
    for row in field:
        print(row)
    print()

codes = []
for field in fields:
    row_codes = []
    col_codes = []
    h = len(field)
    w = len(field[0])

    for i in range(h):
        row_codes.append(encode_row(field, i))

    for j in range(w):
        col_codes.append(encode_col(field, j))
    
    codes.append([row_codes, col_codes])

def fold_index(codes):
    n = len(codes)
    print(codes)
    for i in range(1, n):
        l, r = i-1, i
        is_mirror = True
        while 0 <= l and r < n:
            print(codes[l], codes[r])
            if codes[l] != codes[r]:
                is_mirror = False
                break
            l -= 1
            r += 1
        if is_mirror:
            return i
    return 0
        

part_1 = 0
for r_codes, c_codes in codes:
    n_row = fold_index(r_codes)
    n_col = fold_index(c_codes)
    part_1 += n_col
    part_1 += 100 * n_row

print("Part 1", part_1)