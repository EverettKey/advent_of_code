f_name = "input_1"

def find_number(line):
    ans = 0
    for char in line:
        if char.isdigit():
            ans += int(char)
            ans *= 10
            break
    for i in range(len(line)):
        if line[~i].isdigit():
            ans += int(line[~i])
            break
    return ans



answer = 0
with open(f_name) as f:
    lines = f.readlines()
    for line in lines:
        # print(find_number(line))
        answer += find_number(line)

print("Part 1:", answer)

num_strs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

nums = {}
for i, str in enumerate(num_strs):
    nums[str] = i+1

f2_name = "input_1"

def find_number2(line):
    ans = 0
    digit = None
    for i, char in enumerate(line):
        if char.isdigit():
            digit = int(char)
            break

        for j in range(3,6):
            if 0 <= i - j + 1 and line[i-j+1:i+1] in nums:
                digit = nums[line[i-j+1:i+1]]
                break
        
        if digit: break
        
    ans += digit
    ans *= 10

    digit = None
    for i in range(len(line)-1,-1,-1):
        if line[i].isdigit():
            digit = int(line[i])
            break

        for j in range(3,6):
            if i+j <= len(line) and line[i:i+j] in nums:
                print(line[i:i+j])
                digit = nums[line[i:i+j]]
                break
        
        if digit: break
    return ans + digit

answer = 0
with open(f2_name) as f:
    lines = f.readlines()
    for line in lines:
        plus = find_number2(line)
        print(plus, line)
        answer += plus
print("Part 2:", answer)



for i in range(3,-1): print(i)