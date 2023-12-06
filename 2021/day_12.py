f_name = "input_12"

def add_map(l, r, map):
    if not l in map:
        map[l] = [r]
    else:
        map[l].append(r)

map = {}
with open(f_name) as f:
    lines = f.readlines()
    for line in lines:
        l, r = line.strip("\n").split("-")
        add_map(l, r, map)
        add_map(r, l, map)

seen_routes = set()

q = []
q.append((['start'], set(['start'])))
ans = 0
while q:
    path, walked_small = q.pop()
    childs = map[path[-1]]
    for child in childs:
        if child == 'end':
            print(path)
            ans += 1
        elif child not in walked_small:
            path.append(child)
            if tuple(path) not in seen_routes:
                if child.islower():
                    walked_small.add(child)
                seen_routes.add(tuple(path))
                q.append((path[:], set(walked_small)))
            path.pop()
            if child.islower():
                walked_small.remove(child)

print("Part 1 answer:", ans)

seen_routes = set()

q = []
q.append((['start'], set(['start'])))
ans = 0
while q:
    path, walked_small = q.pop()
    childs = map[path[-1]]
    for child in childs:
        if child == 'end':
            print(path)
            ans += 1
        elif child not in walked_small:
            path.append(child)
            if tuple(path) not in seen_routes:
                if child.islower():
                    walked_small.add(child)
                seen_routes.add(tuple(path))
                q.append((path[:], set(walked_small)))
            path.pop()
            if child.islower():
                walked_small.remove(child)



