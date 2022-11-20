f_name = 'input_5'

with open(f_name) as f:
    lines = f.readlines()

points = set()
big_points = set()

def add_point(point):
    if point in points:
        big_points.add(point)
    else:
        points.add(point)

for line in lines:
    pair = line.strip('\n').split(' -> ')
    x0, y0 = (int(num) for num in pair[0].split(','))
    x1, y1 = (int(num) for num in pair[1].split(','))
    if x0 == x1:
        for i in range(min(y0, y1), max(y0, y1) + 1):
            add_point((x0, i))
    elif y0 == y1:
        for j in range(min(x0, x1), max(x0, x1) + 1):
            add_point((j, y0))

print("Part 1 answer:", len(big_points))

def get_increment(a, b):
    if a == b:
        return 0
    if a < b:
        return 1
    else:
        return -1

# Part 2
points = set()
big_points = set()
for line in lines:
    pair = line.strip('\n').split(' -> ')
    x0, y0 = (int(num) for num in pair[0].split(','))
    x1, y1 = (int(num) for num in pair[1].split(','))
    
    x_incre = get_increment(x0, x1)
    y_incre = get_increment(y0, y1)

    add_point((x0, y0))
    while True:
        if x0 == x1 and y0 == y1:
            break
        x0 += x_incre
        y0 += y_incre
        add_point((x0, y0))

print("Part 2 answer:", len(big_points))



