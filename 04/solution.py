
with open('04/input.txt', 'r') as file:
    input = file.read().strip()

enclosed_ranges = 0
overlapping_ranges = 0

for line in input.split('\n'):
    s1, s2 = [s.split('-') for s in line.split(',')]

    s1, s2 = [[int(n) for n in s.split('-')] for s in line.split(',')]
    
    ############
    ## Part 1 ##
    ############

    if (s1[0] >= s2[0] and s1[1] <= s2[1])\
    or (s2[0] >= s1[0] and s2[1] <= s1[1]):
        enclosed_ranges += 1
    
    ############
    ## Part 2 ##
    ############

    if (s1[1] >= s2[0] and s1[1] <= s2[1])\
    or (s2[1] >= s1[0] and s2[1] <= s1[1]):
        overlapping_ranges += 1

print(enclosed_ranges)
print(overlapping_ranges)
