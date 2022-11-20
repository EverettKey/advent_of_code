# note:
# be aware [set()] * 5 points to the same set!
# use test cases!
# watched tutorial, thought my right answer is wrong
# because answer is different. Not even tried to
# submit it

f_name = 'input_4'

with open(f_name) as f:
    lines = f.readlines()
    guesses = lines[0].strip('\n').split(',')

    boards = []
    for i in range(2, len(lines), 6):
        board = [set() for  i in range(5)]
        for j in range(5):
            line = list(filter(None, lines[i + j].strip('\n ').split(' ')))
            line = [int(item) for item in line]
            board.append(set([int(item) for item in line]))
            for k in range(5):
                board[k].add(line[k])
        boards.append(board)

def calc_score(b, g):
    s = 0
    for line in board:
        s += sum(line)
    score = s // 2 * guess
    return score

s = 0
winner = False
complete_boards = set()
for guess in guesses:
    guess = int(guess)
    for i,  board in enumerate(boards):
        if not i in complete_boards:
            for line in board:
                if guess in line:
                    line.remove(guess)

                    if len(line) == 0:
                        winner = True

            if winner:
                if len(complete_boards) == 0 or len(complete_boards) == len(boards) - 1:
                    print(calc_score(board, guess))
                complete_boards.add(i)
                winner = False

    if len(complete_boards) == len(boards):
        break

            # break


#39 + 87 + 91 + 57 + 85 + 94 + 1+3 +73+44+73+39+44+85+87+3+57+94+1+91