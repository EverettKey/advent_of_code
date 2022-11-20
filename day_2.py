f_name = "input_2"

data = {"forward": [0,1], "down": [1, 1], "up": [1, -1]}
dis_n_dep = [0, 0]

with open(f_name) as f:
    line = f.readline()
    while line:
        command, amount = line.split()
        dis_or_dep, multiplier = data[command]
        dis_n_dep[dis_or_dep] += multiplier * int(amount)
        line = f.readline()
print(dis_n_dep[0] * dis_n_dep[1])

aim = 0
dis = 0
dep = 0

with open(f_name) as f:
    line = f.readline()
    while line:
        command, amount = line.split()
        amount = int(amount)
        if command == 'forward':
            dis += amount
            dep += aim * amount
        
        elif command == 'down':
            aim += amount

        elif command == 'up':
            aim -= amount
        line = f.readline()
print(dis * dep)



