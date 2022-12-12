import re


with open('07/input.txt', 'r') as file:
    input = file.read().strip()

lines = input.splitlines()
files = []

abs_path = []
for line in lines:

    file = re.findall("(\d+)\s(\w+\.?\w+)", line)
    if file:
        size, filename = file[0]
        abs_path.append(filename)
        files.append(('/'.join(abs_path), int(size)))
        abs_path.pop()

    elif line.startswith('$ cd'):
        path = line[5:]  # Remove "$ cd "

        if path == '/':
            abs_path.clear()
        elif path == "..":
            abs_path.pop()
        else:
            abs_path.append(path)

dir_sizes = {
    "/": 0
}

for fp, size in files:
    dir_sizes["/"] += size

    split_path = fp.split('/')[:-1]
    for level in range(1, len(split_path)+1):
        root = '/'.join(split_path[0:level])

        try:
            dir_sizes[root] += size
        except KeyError:
            dir_sizes[root] = size

############
## Part 1 ##
############
s1 = 0
for bytes in dir_sizes.values():
    if bytes <= 100000:
        s1 += bytes

print(s1)

############
## Part 2 ##
############
free = 70000000 - dir_sizes["/"]
deficit = 30000000 - free
delete = []

for bytes in dir_sizes.values():
    if bytes >= deficit:
        delete.append(bytes)
s2 = min(delete)

print(s2)
