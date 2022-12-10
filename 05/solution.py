import re
from copy import deepcopy


stacks = {
    "1": ["G", "D", "V", "Z", "J", "S", "B"],
    "2": ["Z", "S", "M", "G", "V", "P"],
    "3": ["C", "L", "B", "S", "W", "T", "Q", "F"],
    "4": ["H", "J", "G", "W", "M", "R", "V", "Q"],
    "5": ["C", "L", "S", "N", "F", "M", "D"],
    "6": ["R", "G", "C", "D"],
    "7": ["H", "G", "T", "R", "J", "D", "S", "Q"],
    "8": ["P", "F", "V"],
    "9": ["D", "R", "S", "T", "J"]
}

with open('05/input.txt', 'r') as file:
    input = file.read().strip()

instructions = [line for line in input.split('\n') if line.startswith('move')]

s1 = deepcopy(stacks)
s2 = deepcopy(stacks)

for instruction in instructions:
    # how many crates, from stack, to stack
    n_crates, fs, ts = re.findall('\d+', instruction)
    n_crates = int(n_crates)

    ############
    ## Part 1 ##
    ############
    for crate in range(0, n_crates):
        s1[ts].append(s1[fs].pop(-1))

    ############
    ## Part 2 ##
    ############
    s2[ts].extend(s2[fs][-n_crates:])
    s2[fs] = s2[fs][:-n_crates]

for answer in [s1, s2]:
    print(''.join([answer[s][-1] for s in answer]))
