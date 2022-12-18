
with open('08/input.txt', 'r') as file:
    input = file.read().strip()

rows = [list(map(int, line)) for line in input.splitlines()]
columns = [[row[i] for row in rows] for i in range(len(rows))]

visible_trees = 0
view_scores = []

for row_n, row in enumerate(rows):

    for i in range(len(row)):
        tree = row[i]

        n = columns[i][:row_n]
        w = row[:i]
        e = row[i+1:]
        s = columns[i][row_n+1:]

        ############
        ## Part 1 ##
        ############
        if len(n) == 0 or len(w) == 0 or \
        len(e) == 0 or len(s) == 0:
            visible_trees += 1
        elif max(n) < tree or max(w) < tree or \
        max(e) < tree or max(s) < tree:
            visible_trees += 1
        
        ############
        ## Part 2 ##
        ############
        # reverse north and south to standardise iteration order
        n.reverse()
        w.reverse()

        views = []
        for direction in [n, w, e, s]:
            if len(direction) == 0:
                views.append(0)
                continue
            for k, nt in enumerate(direction):
                if nt < tree and k < len(direction)-1:
                    continue
                views.append(k+1)
                break
        
        view_scores.append(views[0] * views[1] * views[2] * views[3])

                    
print(visible_trees)
print(max(view_scores))
