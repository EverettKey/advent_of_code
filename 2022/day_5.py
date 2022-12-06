f_n = 'input_5'
f_n_test = 'input_5_t'

def get_stacks(f_n):
    with open(f_n) as f:
        line = f.readline().strip('\n')
        n_stacks = (len(line) + 1) // 4
        stacks = [[] for i in range(n_stacks)]
        while line:
            if line[1] == '1':
                break
            for i in range(n_stacks):
                pos = i * 4 + 1
                if not line[pos] == ' ':
                    stacks[i].append(line[pos])
            line = f.readline().strip('\n')
    return stacks

def get_moves(f_n):
    with open(f_n) as f:
        line = f.readline().strip('\n')
        while 0 < len(line):
            line = f.readline().strip('\n')
        
        moves = []
        line = f.readline().strip('\n')
        while line:
            moves.append([int(num) for num in line.split(' ')[1::2]])
            line = f.readline().strip('\n')
    return moves

def move1(stacks, stack_i, stack_f):
    item = stacks[stack_i - 1].pop(0)
    stacks[stack_f - 1].insert(0, item)

def part_1(f_n):
    stacks = get_stacks(f_n)
    moves = get_moves(f_n)
    for n, stack_i, stack_f in moves:
        for i in range(n):
            move1(stacks, stack_i, stack_f)
    ans = ""
    for stack in stacks:
        ans += stack[0]
    print("Part 1 answer:", ans)

def part_2(f_n):
    stacks = get_stacks(f_n)
    moves = get_moves(f_n)
    for n, i, f in moves:
        sub_stack = stacks[i - 1][:n]
        stacks[f - 1] = sub_stack + stacks[f - 1]
        stacks[i - 1] = stacks[i-1][n:]

    ans = ""
    for stack in stacks:
        ans += stack[0]
    print("Part 1 answer:", ans)


print("=== TESTS ===")
part_1(f_n_test)
part_2(f_n_test)

print("=== RESULTS ===")
part_1(f_n)
part_2(f_n)
            