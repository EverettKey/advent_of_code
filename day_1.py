f_name = 'input'

n_increase = 0
with open(f_name) as f:
    prev = f.readline()
    if prev:
        prev = int(prev)
    cur = f.readline()
    while cur:
        int_cur = int(cur)
        if int_cur > prev:
            n_increase += 1
        prev = int_cur
        cur = f.readline()
print(n_increase)

n_increase_2 = 0
width = 3
mem = []
with open(f_name) as f:
    line = f.readline()
    for i in range(3):
        mem.append(int(line))
        line = f.readline()
    
    while line:
        new_num = int(line)
        if new_num > mem[0]:
            n_increase_2 += 1
        mem.pop(0)
        mem.append(new_num)
        line = f.readline()
print(n_increase_2)

    



