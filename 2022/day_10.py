f_name = "input_10"

targets = [i for i in range(20, 221, 40)]
answer = 0
cycle = 0
X = 1

def add_cycle(cycle, answer):
    cycle += 1
    if cycle in targets:
        answer += cycle * X
        print(cycle, X)
        print(answer)
    return (cycle, answer)

with open(f_name) as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        parts = line.strip('\n').split(" ")

        cycle, answer = add_cycle(cycle, answer)
        if len(parts) > 1:
            cycle, answer = add_cycle(cycle, answer)
            X += int(parts[1])
print("Part 1 answer: ", answer)

display = ""
answer = 0
cycle = 0
X = 1

def display_cycle(cycle, answer, display):
    cycle += 1
    if X <= cycle % 40 < X + 3:
        display += "#"
    else:
        display += "."
    if cycle in targets:
        answer += cycle * X
    return (cycle, answer, display)

with open(f_name) as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        parts = line.strip('\n').split(" ")
        cycle, answer, display = display_cycle(cycle, answer, display)
        if len(parts) > 1:
            cycle, answer, display = display_cycle(cycle, answer, display)
            X += int(parts[1])

for i in range(6):
    print(display[i * 40:(i + 1) *40])