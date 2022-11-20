f_name = 'input_6'

with open(f_name) as f:
    data = f.readline().strip('\n').split(',')

# 8 days -> mod 9
born_wait_time = 9
# 6 days -> +7
rest_time = 7

n_days = 256



def count_fish(fishes, n_days):
    for i in range(n_days):
        index = i % born_wait_time
        rest_fish = fishes[index]
        rest_fish_index = (index + rest_time) % born_wait_time
        fishes[rest_fish_index] += rest_fish
    return sum(fishes)

fishes1 = [0] * born_wait_time
for fish in data:
    fishes1[int(fish)] += 1

print("Part 1 answer:", count_fish(fishes1, 80))

fishes2 = [0] * born_wait_time
for fish in data:
    fishes2[int(fish)] += 1
print("Part 2 answer:", count_fish(fishes2, 256))
