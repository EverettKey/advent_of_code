import math
f_name = "input_8"

directions = None
map = {}

with open(f_name) as f:
    lines = f.readlines()
    directions = lines[0].strip('\n')
    for line in lines[2:]:
        start, eq, l, r = line.strip('\n').split(' ')
        lr = [l[1:4], r[:3]]
        map[start] = lr

cur = 'AAA'
dir_idx = 0
part_1 = 0

lr_trans = {'L': 0, 'R': 1}
while not cur == 'ZZZ':
    direction = directions[dir_idx]
    direction_idx = lr_trans[direction]
    cur = map[cur][direction_idx]
    part_1 += 1
    dir_idx += 1
    dir_idx %= len(directions)
print("part 1:", part_1)



f_name = "input_8"

directions = None
map = {}

with open(f_name) as f:
    lines = f.readlines()
    directions = lines[0].strip('\n')
    for line in lines[2:]:
        start, eq, l, r = line.strip('\n').split(' ')
        lr = [l[1:4], r[:3]]
        map[start] = lr


starts = []
for start, ends in map.items():
    if start[-1] == 'A':
        starts.append(start)

n_step = 0
dir_idx = 0



n_steps = [0] * len(starts)
while True:
    direction = directions[dir_idx]
    direction_idx = lr_trans[direction]
    # print(starts)

    n_step += 1

    n_Zs = 0
    for i, start in enumerate(starts):
        end = map[start][direction_idx]
        starts[i] = end
        
        if end[-1] == 'Z' and n_steps[i] == 0:
            n_steps[i] = n_step
    
    dir_idx += 1
    dir_idx %= len(directions)

    # if part_2 == 10: break
    if 0 not in n_steps: break

print(n_steps)
part_2 = 1
for n in n_steps:
    part_2 = math.lcm(n, part_2)
print("Part 2:", part_2)

