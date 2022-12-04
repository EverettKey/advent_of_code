f_n = 'input_2'
f_n_t = 'input_2_t'

p1_score_map = {'A': 1, 'B': 2, 'C': 3}
p2_score_map = {'X': 1, 'Y': 2, 'Z': 3}
result_score_map = {'X': 0, 'Y': 1, 'Z': 2}

def parse_input(f_name):
    matches = []
    with open(f_name) as f:
        line = f.readline()
        while line:
            matches.append(line.strip('\n').split(' '))
            line = f.readline()
    return matches

def part1(matches):
    score = 0
    for p1, p2 in matches:
        p1_score = p1_score_map[p1]
        p2_score = p2_score_map[p2]
        win_score = (p2_score - p1_score + 1) % 3 * 3

        score += p2_score
        score += win_score
        
    print("Part 1 answer:", score)



def part2(matches):
    score = 0
    for p1, res in matches:
        p1_score = p1_score_map[p1]
        result = result_score_map[res]

        p2_score =  (p1_score + result + 1) % 3 + 1
        result_score = result * 3

        score += p2_score + result_score

    print("Part 2 answer:", score)

    

data_t = parse_input(f_n_t)
data = parse_input(f_n)

print("=== TESTS ===")
part1(data_t)
part2(data_t)

print("=== RESULTS ===")
part1(data)
part2(data)