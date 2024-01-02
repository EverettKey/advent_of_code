from collections import Counter
f_name = 'input_12'

rows = []
streaks = []
with open(f_name) as f:
    lines = f.readlines()
    for line in lines:
        wells_str, streaks_str = line.strip('\n').split(' ')
        rows.append(list(wells_str))
        streaks.append([int(x) for x in streaks_str.split(',')])
print(rows)
print(streaks)

max_unknows = 0
for row in rows:
    max_unknows = max(max_unknows, Counter(row)['?'])
print("max number of ?s:", max_unknows)

def is_good_guess(str, parts):
    segs_len = [len(seg) for seg in str.split('.') if seg != '']
    return segs_len == parts

def count_guesses(row, parts):
    pos = []
    for i, spring in enumerate(row):
        if spring == '?':
            pos.append(i)
    
    
    

part_1 = 0


for i, row in enumerate(rows):
    


print("Part_1", part_1)
# 21