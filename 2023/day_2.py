f_name = "input_2_t"

part_1 = 0
# 12 red cubes, 13 green cubes, and 14 blue cubes?
r_limit = 12
g_limit = 13
b_limit = 14
limits = {'r': r_limit, 'g': g_limit, 'b': b_limit}
with open(f_name) as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        game = line.strip("\n").split(":")[1].split(";")
        ilegal = False
        for hand in game:
            piles = hand.strip(' ').split(', ')
            print(piles)
            for pile in piles:
                n, color = pile.split(' ')
                if limits[color[0]] < int(n):
                    ilegal = True
                    break
            if ilegal: break
        if not ilegal:
            part_1 += i + 1
print("Part 1:", part_1)


with open(f_name) as f:
    lines = f.readlines()
    part_2 = 0
    for i, line in enumerate(lines):
        game = line.strip("\n").split(":")[1].split(";")
        mins = {'r': 0, 'g': 0, 'b': 0}
        for hand in game:
            piles = hand.strip(' ').split(', ')
            for pile in piles:
                n, color = pile.split(' ')
                mins[color[0]] = max(int(n), mins[color[0]])
        power = 1
        for c in 'rgb':
            power *= mins[c]
        part_2 += power
print("part 2:", part_2)
        
            

                
