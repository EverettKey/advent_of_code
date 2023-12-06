import numpy as np
f_name = "input_9"
dir_map = {"R": (0, 1), "U": (-1, 0), "D": (1, 0), "L": (0, -1)}
instruction = []
with open(f_name) as f:
    lines = f.readlines()
    for line in lines:
        dir, steps = line.strip("\n").split(" ")
        for i in range(int(steps)):
            instruction.append(dir_map[dir])

def move(head, step):
    r, c = step
    head[0] += r
    head[1] += c
    return head

def follow(head, tail):
    r_diff = head[0] - tail[0]
    c_diff = head[1] - tail[1]
    if abs(r_diff) == 2:
        tail[0] += np.sign(r_diff)
        if abs(c_diff) == 1:
            tail[1] += c_diff

    if abs(c_diff) == 2:
        tail[1] += np.sign(c_diff)
        if abs(r_diff) == 1:
            tail[0] += r_diff
    return tail
    

s = set()
s.add((0,0))
tail = [0, 0]
head = [0, 0]
for step in instruction:
    head = move(head, step)
    tail = follow(head, tail)
    s.add(tuple(tail))


print("Part 1 answer:", len(s))

s2 = set()
s2.add((0,0))

links = [[0,0] for i in range(10)]
for step in instruction:
    links[0] = move(links[0], step)
    for i in range(1,10):
        links[i] = follow(links[i-1], links[i])
    s2.add(tuple(links[-1]))

print("Part 2 answer:", len(s2))