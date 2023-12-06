f_name = "input_14"

rocks = set()
bot_bound = 0

def draw_rock(coord1, coord2):
    global bot_bound
    if coord1:
        c1, r1 = coord1
    else:
        c1, r1 = coord2
    c2, r2 = coord2
    for i in range(min(r1, r2), max(r1, r2) + 1):
        for j in range(min(c1, c2), max(c1, c2) + 1):
            rocks.add((i, j))
            bot_bound = max(bot_bound, i)

def find_next(coord):
    r, c = coord
    for new_r, new_c in [(r+1, c), (r+1, c-1), (r+1, c+1), (r, c)]:
        if not (new_r, new_c) in rocks:
            return (new_r, new_c)


with open(f_name) as f:
    lines = f.readlines()
    for line in lines:

        points_str = line.strip('\n').split(' -> ')
        prev_point = None
        for point_str in points_str:
            point = [int(str) for str in point_str.split(',')]
            draw_rock(prev_point, point)
            prev_point = point

sand_count = 0

origin = (0, 500)
sand = origin
while True:
    new_sand = find_next(sand)
    # print(sand, new_sand, sand == new_sand)
    if bot_bound <= new_sand[0]:
        break

    if new_sand == sand:
        rocks.add(sand)
        sand_count += 1
        sand = origin
    else:
        sand = new_sand

print(f"There are {sand_count} blocks of sand.")

rocks = set()
with open(f_name) as f:
    lines = f.readlines()
    for line in lines:

        points_str = line.strip('\n').split(' -> ')
        prev_point = None
        for point_str in points_str:
            point = [int(str) for str in point_str.split(',')]
            draw_rock(prev_point, point)
            prev_point = point

print(bot_bound)

sand_count = 0
sand = origin
while True:
    # break
    new_sand = find_next(sand)
    # print(sand, new_sand, sand == new_sand)

    if new_sand == sand or sand[0] == bot_bound + 1:
        rocks.add(sand)
        print(sand, new_sand==sand, sand[0] == bot_bound + 1)
        sand_count += 1
        if new_sand == origin:
            break
        sand = origin
    else:
        sand = new_sand

print(f"Part 2 has {sand_count} blocks of sand.")





        
