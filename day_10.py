f_name = "input_10"

score_table = {')': 3, 
               ']': 57,
               '}': 1197,
               '>': 25137}

open_chars = set('([{<')

match_table = {')': '(', 
               ']': '[',
               '}': '{',
               '>': '<'}

data = []
with open(f_name) as f:
    data = [line.strip('\n') for line in f.readlines()]

def calc_line_score1(line):
    stak = []
    for i, char in enumerate(line):
        if char in open_chars:
            stak.append(char)
        else:
            if match_table[char] == stak[-1]:
                stak.pop()
            else:
                return score_table[char]
    return 0

score = 0
for line in data:
    score += calc_line_score1(line)

print("Part 1 answer:", score)

score_table2 = {'(': 1, 
               '[': 2,
               '{': 3,
               '<': 4}

def calc_line_score2(line):
    stak = []
    for i, char in enumerate(line):
        if char in open_chars:
            stak.append(char)
        else:
            if match_table[char] == stak[-1]:
                stak.pop()
            else:
                return 0
    
    score = 0
    for char in reversed(stak):
        score *= 5
        score += score_table2[char]
    return score

scores = []
for line in data:
    line_score = calc_line_score2(line)
    if 0 < line_score:
        scores.append(line_score)

scores.sort()
winner = scores[len(scores)//2]
print("Part 2 answer:", winner)

