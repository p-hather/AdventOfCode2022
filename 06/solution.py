
with open('06/input.txt', 'r') as file:
    input = file.read().strip()

############
## Part 1 ##
############
for pos in range(4, len(input)):
    seq = input[pos-4:pos]
    if len(seq) == len(set(seq)):
        print(pos)
        break

############
## Part 1 ##
############
for pos in range(14, len(input)):
    seq = input[pos-14:pos]
    if len(seq) == len(set(seq)):
        print(pos)
        break
