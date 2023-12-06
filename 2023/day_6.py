import math
f_name = "input_6"

part_1 = 1
part_2 = 0

lines = []

with open(f_name) as f:
    lines = f.readlines()
    ts, ds = lines[0], lines[1]

times = [int(x) for x in ts.strip('\n').split(':')[1].split()]
distances = [int(x) for x in ds.strip('\n').split(':')[1].split()]

print(times)
print(distances)

'''
d = x * (t - x)
D < d

D < x * (t - x)
D < xt - x^2
0 < xt - x^2 - D 

solve: 
0 =  -x^2 + xt - D
'''
for i in range(len(times)):
    D = distances[i]
    t = times[i]
    n = 0
    for j in range(t+1):
        if D < j * (t - j):
            n += 1
    part_1 *= n

print("Part_1", part_1)

time = int(''.join(ts.strip('\n').split(':')[1].split()))
distance = int(''.join(ds.strip('\n').split(':')[1].split()))

print(time, distance)


n2 = 0
for i in range(time+1):
    if distance < i * (time-i):
        n2 += 1

print("Part_2", n2)
