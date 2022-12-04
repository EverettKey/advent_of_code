f_n = 'input_4'
f_n_test = 'input_4_t'

def get_pairs(f_name):
    pairs = []
    with open(f_name) as f:
        line = f.readline()
        while line:
            a, b = line.strip('\n').split(',')
            a_range = [int(point) for point in a.split('-')]
            b_range = [int(point) for point in b.split('-')]
            pairs.append([a_range, b_range])
            line = f.readline()
    return pairs

def part_1(f_name):
    pairs = get_pairs(f_name)
    ans = 0
    for a, b in pairs:
        if b[0] <= a[0] and a[1] <= b[1]:
            ans += 1
        elif a[0] <= b[0] and b[1] <= a[1]:
            ans += 1
    print("Part 1 answer:", ans)

def part_2(f_name):
    pairs = get_pairs(f_name)
    ans = 0
    for a, b in pairs:
        if b[0] <= a[1] and a[0] <= b[1]:
            ans += 1
    print("Part 2 answer:", ans)

print("=== TESTS ===")
part_1(f_n_test)
part_2(f_n_test)

print("=== RESULTS ===")
part_1(f_n)
part_2(f_n)
            

