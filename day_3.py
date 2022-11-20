from email.utils import collapse_rfc2231_value
from math import gamma


input_f = 'input_3'

line_len = -1
memory = []
with open(input_f) as f:
    line = f.readline()
    while line:
        if line_len < 0:
            line_len = len(line) - 1 # get rid of newline
            memory = [0] * line_len 

        for i, digit in enumerate(line.split()[0]):
            if digit == '1':
                memory[i] += 1
            else:
                memory[i] -= 1
        line = f.readline()

gam = 0 # 0 < digit, more 1
eps = 0 # digit < 0, more 0
print(memory)
for digit in memory:
    gam *= 2
    eps *= 2
    if 0 < digit:
        gam += 1
    else:
        eps += 1
    if digit == 0:
        print(digit)

print(gam * eps) 


# Part 2
with open(input_f) as f:
    data = [line for line in f.read().strip().split('\n')]

width = len(data[0])

big_set = set(tuple(line) for line in data)
oxy_set = big_set
co2_set = big_set.copy()

i = 0
while 1 < len(oxy_set):
    set_1 = set()
    set_0 = set()
    for line in oxy_set:
        if line[i] == '1':
            set_1.add(line)
        else:
            set_0.add(line)
    if len(set_0) > len(set_1):
        oxy_set = set_0
    else:
        oxy_set = set_1
    i += 1

i = 0
while 1 < len(co2_set):
    set_1 = set()
    set_0 = set()
    for line in co2_set:
        if line[i] == '1':
            set_1.add(line)
        else:
            set_0.add(line)
    if len(set_0) > len(set_1):
        co2_set = set_1
    else:
        co2_set = set_0
    i += 1

print(oxy_set)
print(co2_set)

oxy = int(''.join(oxy_set.pop()), 2)
co2 = int(''.join(co2_set.pop()), 2)

print('oxy = ', oxy)
print('co2 = ', co2)
print(oxy * co2)