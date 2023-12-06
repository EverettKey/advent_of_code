f_name = "input_8"

with open(f_name) as f:
    data = f.readlines()

unique_lens = set([2, 4, 3, 7])
unique_lens_table = {2:1, 3:7, 4:4, 7:8}

part_1_ans = 0
for line in data:
    output = line.split('|')[1].strip(' \n').split(' ')
    for digit in output:
        if len(digit) in unique_lens:
            part_1_ans += 1

print("Part 1 answer:", part_1_ans)


'''
Part 2
'''


def decode_unique(uniques, unique):
    table = [[] for i in range(8)]

# 2, 3 5
# overlaps
#    1   4
# 2  1   2
# 3  2   3
# 5  1   3
def decode_5(uniques, code):
    count1 = 0
    count4 = 0
    for char in code:
        if char in uniques[1]:
            count1 += 1
        if char in uniques[4]:
            count4 += 1
    if count1 == 2:
        return 3
    elif count4 == 2:
        return 2
    return 5

# 0, 6, 9
def decode_6(uniques, code):
    for char in uniques[1]:
        if char not in code:
            return 6
    for char in uniques[4]:
        if char not in code:
            return 0
    return 9

ans2 = 0
for line in data:
    all10, input = line.split('|')
    all10 = all10.strip(' \n').split(' ')
    input = input.strip(' \n').split(' ')
    uniques = {}
    for code in all10:
        if len(code) in unique_lens:
            decode = unique_lens_table[len(code)]
            uniques[decode] = set(code)

    num = 0
    for code in input:
        num *= 10
        if len(code) in unique_lens:
            num += unique_lens_table[len(code)]
        elif len(code) == 5:
            num += decode_5(uniques, code)
        else:
            num += decode_6(uniques, code)
    ans2 += num

print("Part 2 answer:", ans2)
        