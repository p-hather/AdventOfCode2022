
with open('./03/input.txt', 'r') as file:
    input = file.read().strip()

lines = input.split('\n')

############
## Part 1 ##
############

priority_p1 = 0

for line in lines:
    items = list(line)
    midpoint = int(len(items)/2)
    c1, c2 = set(items[:midpoint]), set(items[midpoint:])
    
    item = c1.intersection(c2).pop()
    lowercase = item.lower()
    priority = ord(lowercase) - 96
    if item.isupper():
        priority += 26
    
    priority_p1 += priority

print(priority_p1)


############
## Part 2 ##
############

priority_p2 = 0

def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

thruples = list(split_list(lines, 3))

for t in thruples:
    c1, c2, c3 = set(t[0]), set(t[1]), set(t[2])
    item = c1.intersection(c2, c3).pop()
    lowercase = item.lower()
    priority = ord(lowercase) - 96
    if item.isupper():
        priority += 26
    
    priority_p2 += priority

print(priority_p2)
