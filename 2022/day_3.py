f_n = 'input_3'
f_n_t = 'input_3_t'

a_base = ord('a')
A_base = ord('A')
def parse_data(f_name):
    data = []
    with open(f_name) as f:
        data = f.readlines()
    return data

def get_priority(item):
    if item.islower():
        return ord(item) - a_base + 1
    else:
        return ord(item) - A_base + 1 + 26

def inspect_sack(left, right):
    left_set = set(left)
    for item in right:
        if item in left_set:
            return get_priority(item)

    print("No repeats!")
    return 0

def find_badge(lines):
    set1 = set(lines[0])
    set2 = set(lines[1])
    for item in lines[2]:
        if item in set1 and item in set2:
            return item
    print("No Badge!")
    return 'a'

def part1(data):
    sum = 0
    for line in data:
        cut = len(line.strip('\n')) // 2
        sum += inspect_sack(line[:cut], line[cut:])
    print("Part 1 answer:", sum)


def part2(data):
    score = 0
    for i in range(0, len(data), 3):
        badge = find_badge(data[i: i+3])
        score += get_priority(badge)
    print("Part 2 answer:", score)

test_data = parse_data(f_n_t)
data = parse_data(f_n)


print("=== TESTS ===")
part1(test_data)
part2(test_data)

print("=== RESULTS ===")
part1(data)
part2(data)