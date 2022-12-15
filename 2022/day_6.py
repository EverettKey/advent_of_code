f_name = "input_6"

def add_char(char, d):
    if char in d:
        d[char] += 1
    else:
        d[char] = 1
    

def remove_char(char, d):
    d[char] -= 1
    if d[char] == 0:
        del d[char]

def find_unique(f_name, l):
    d = {}
    with open(f_name) as f:
        line = f.readline()
        i = 0
        j = 0
        for k in range(l):
            char = line[k]
            add_char(char, d)
        
        for k in range(l, len(line)):
            if len(d) == l:
                return k
            else:
                char_head = line[k]
                char_tail = line[k-l]
                add_char(char_head, d)
                remove_char(char_tail, d)

print("Part 1 answer:", find_unique(f_name, 4))
print("Part 2 answer:", find_unique(f_name, 14))
    