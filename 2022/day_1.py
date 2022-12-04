f_name = 'input_1'

with open(f_name) as f:
    lines = f.readlines()

max_cal = 0
cur_cal = 0

top_elves = [0] * 3

for i, line in enumerate(lines):
    str = line.strip('\n')
    if len(str) == 0:
        max_cal = max(max_cal, cur_cal)
        if top_elves[0] < cur_cal:
            top_elves.append(cur_cal)
            top_elves.sort()
            top_elves.pop(0)
        cur_cal = 0
    else:
        cur_cal += int(str)

max_cal = max(max_cal, cur_cal)
if top_elves[0] < cur_cal:
    top_elves.append(cur_cal)
    top_elves.sort()
    top_elves.pop(0)
print('Part 1 answer:', max_cal)

print('Part 2 answer:', sum(top_elves))


