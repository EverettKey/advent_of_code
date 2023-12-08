from collections import Counter
f_name = "input_7"

ranks = "AKQJT98765432"
rank_table = {}
for i, char in enumerate(ranks):
    rank_table[char] = i

lines = None
with open(f_name) as f:
    lines = f.readlines()

data = []

'''
0 5
1 4
2 3-2
3 3-1-1
4 2-2-1
5 2-1-1-1
6 1-1-1-1
'''
for line in lines:
    cards, bet = line.strip('\n').split()
    hand_info = []
    c = Counter(cards)
    counts = sorted(item[1] for item in c.items())
    rank = [-x for x in counts[::-1]]
    hand_info.append(tuple(rank))

    digit_hand = []
    for card in cards:
        digit_hand.append(rank_table[card])
    hand_info.append(tuple(digit_hand))

    hand_info.append(int(bet))

    data.append(tuple(hand_info))

data.sort()
score = 0
n = len(data)
for i in range(len(data)):
    score += data[i][2] * (n-i)
part_1 = score


# test answer 6440
# 252578423 too high
print("part_1:", part_1)

ranks = "AKQT98765432J"
rank_table = {}
for i, char in enumerate(ranks):
    rank_table[char] = i
data = []
for line in lines:
    cards, bet = line.strip('\n').split()
    hand_info = []
    c = Counter(cards)
    n_wild = 0
    if 'J' in c:
        n_wild = c['J']
        del c['J']

    counts = sorted(item[1] for item in c.items())
    if n_wild == 5:
        counts.append(5)
    else:
        counts[-1] += n_wild
    rank = [-x for x in counts[::-1]]
    hand_info.append(tuple(rank))

    digit_hand = []
    for card in cards:
        digit_hand.append(rank_table[card])
    hand_info.append(tuple(digit_hand))

    hand_info.append(int(bet))

    data.append(tuple(hand_info))


data.sort()
score = 0
n = len(data)
for i in range(len(data)):
    print(data[i])
    score += data[i][2] * (n-i)
part_2 = score

# test anaswer 5905
# 249144436 too low
print("part 2:", part_2)