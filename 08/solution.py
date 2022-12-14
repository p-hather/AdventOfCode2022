
with open('08/input.txt', 'r') as file:
    input = file.read().strip()

rows = [list(map(int, line)) for line in input.splitlines()]
columns = [[row[i] for row in rows] for i in range(len(rows))]

visible_trees = 0

for row_n, row in enumerate(rows):
    # outside north or south rows
    if row_n == 0 or row_n == len(rows)-1:
        visible_trees += len(row)
        continue

    for i in range(len(row)):
        # outside east or west columns
        if i == 0 or i == len(row)-1:
            visible_trees += 1
            continue

        tree = row[i]

        n = columns[i][:row_n]
        e = row[i+1:]
        s = columns[i][row_n+1:]
        w = row[:i]

        if max(n) < tree or max(e) < tree or \
        max(s) < tree or max(w) < tree:
            visible_trees += 1

print(visible_trees)
