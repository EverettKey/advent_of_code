f_name = "input_5"

part_1 = 0
part_2 = 0

lines = []

with open(f_name) as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        
seeds = [int(x) for x in lines[0].split(':')[1].strip().split()]

data = []
formula = []
i = 3
while i < len(lines):
    line = lines[i]
    if len(line) == 1:
        data.append(formula)
        formula = []
        i += 2
    else:
        formula.append([int(x) for x in line.strip("\n").split()])
        i += 1
data.append(formula)

print(data)

for formula in data:
    new_seeds = []
    for seed in seeds:
        transformed = False
        for dest_start, source_start, trans_range in formula:
            if source_start <= seed < source_start + trans_range:
                new_seeds.append(dest_start + (seed - source_start))
                transformed = True
                break
        if not transformed:
            new_seeds.append(seed)
    seeds = new_seeds


part_1 = min(seeds)
    


print("Part 1:", part_1)


print("Part 2:", part_2)