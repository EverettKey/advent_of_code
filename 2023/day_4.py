f_name = "input_4"

data = []
with open(f_name) as f:
    lines = f.readlines()
    for line in lines:
        l_str, r_str = line.strip('\n').split(':')[1].split('|')
        l = l_str.strip().split()
        r = r_str.strip().split()
        data.append([l, r])

part_1 = 0
scores = []
for l, r in data:
    l_nums = set()
    for num_str in l:
        n = int(num_str)
        l_nums.add(n)
    power = -1
    for num_str in r:
        if int(num_str) in l_nums:
            power += 1
    score = 0
    if -1 < power:
        score = power + 1
        part_1 += 2 ** power
    scores.append(score)
    

# test: 13
print("Part 1:", part_1)

cards =[1] * len(data)

i = 0
while i < len(scores):
    score = scores[i]
    multiplier = cards[i]
    for j in range(i+1, min(len(scores), i+score+1)):
        cards[j] += multiplier
    i += 1
    
part_2 = sum(cards)
# test: 30
print("Part 2:", part_2)