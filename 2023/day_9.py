f_name = "input_9"
# f_name = "input_9_t"

data = []
with open(f_name) as f:
    lines = f.readlines()
    for line in lines:
        data.append([int(x) for x in line.strip('\n').split()])


def predict(seq):
    if all(x == 0 for x in seq): # can't use sum(seq) because it may be [-1, 1]
        return 0
    
    diffs = [seq[i] - seq[i-1] for i in range(1,len(seq))]
    print(diffs)
    return seq[-1] + predict(diffs)

predictions = []
for seq in data:
    prediction = predict(seq)
    predictions.append(prediction)

print(predictions)
part_1 = sum(predictions)

#114 
# 1955513110 too high
# 1955513104
print("Part_1:", part_1)

def revdict(seq):
    if all(x == 0 for x in seq): # can't use sum(seq) because it may be [-1, 1]
        return 0
    
    diffs = [seq[i] - seq[i-1] for i in range(1,len(seq))]
    print(diffs)
    return seq[0] - revdict(diffs)

revdictions = []
for seq in data:
    revdiction = revdict(seq)
    revdictions.append(revdiction)

print(revdictions)
part_2 = sum(revdictions)
print("Part 2:", part_2)