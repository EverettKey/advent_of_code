f_name = 'input_7'

crabs = []
with open(f_name) as f:
    line = f.readline()
    data = line.strip('\n').split(',')
    for datum in data:
        crabs.append(int(datum))


crabs.sort()
median = crabs[len(crabs)//2]
print(median)

fuel = 0
for crab in crabs:
    fuel += abs(crab - median)

print("Part 1 answer:", fuel)


def find_cost2(crabs, mean):
    cost = 0
    for crab in crabs:
        d = abs(crab - mean)
        cost += d * (d+1) // 2
    return cost

mean1 = sum(crabs) // len(crabs)
mean2 = mean1 + 1

cost1 = find_cost2(crabs, mean1)
cost2 = find_cost2(crabs, mean2)


print("Part 2 answer", min(cost1, cost2))