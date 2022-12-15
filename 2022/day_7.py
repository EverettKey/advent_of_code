import math
test_name = "input_7"

small_dirs = set()

class Dir:
    def __init__(self, name, parent=None) -> None:
        self.sub_files = []
        self.childs = {}
        self.size = 0
        self.parent = parent
        if self.parent:
            self.name = self.parent.name + '/' + name
        else:
            self.name = name
        all_dirs.add(self)
        small_dirs.add(self)

    def add_size(self, amount):
        self.size += amount
        if 100000 < self.size and self in small_dirs:
            small_dirs.remove(self)

        if self.parent:
            self.parent.add_size(amount)
    
    def add_child(self, name):
        new_child = Dir(name, self)
        self.childs[name] = new_child

all_dirs = set()
cur_dir = Dir('/')
root_dir = cur_dir
answer = 0

def is_list_item(line):
    return not len(line) == 0 and not line[0] == '$'

def run_list(f):
    line = f.readline().strip('\n')
    while is_list_item(line):
        items = line.split(' ')
        if items[0] == 'dir':
            cur_dir.add_child(items[1])
        else:
            cur_dir.add_size(int(items[0]))

        line = f.readline().strip('\n')
    return line

def run_command(line, f):
    global cur_dir
    global root_dir
    items = line.split(' ')
    if items[1] == 'ls':
        line = run_list(f) 
    else: 
        destination = items[2]
        if destination == '..':
            cur_dir = cur_dir.parent
        elif destination == '/':
            cur_dir = root_dir
        else:
            cur_dir = cur_dir.childs[destination]
        line = f.readline().strip('\n')
    return line



with open(test_name) as f:
    line = f.readline().strip('\n')
    while line:
        if line[0] == "$":
            line = run_command(line, f)
        else:
            print("Something's wrong??")

part1_ans = 0
for d in small_dirs:
    part1_ans += d.size
print("Part 1 answer:", part1_ans)

total_space = 70000000
need_space  = 30000000
space_limit = total_space - need_space
all_size = root_dir.size
exceed_size = all_size - space_limit

part2_ans = math.inf
for d in all_dirs:
    if exceed_size <= d.size and d.size < part2_ans:
        part2_ans = d.size

print("Part 2 answer:", part2_ans)