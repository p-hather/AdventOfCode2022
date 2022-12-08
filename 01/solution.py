
with open('./01/input.txt', 'r') as file:
    calorie_input = file.read()

calorie_groups = calorie_input.split('\n\n')

calorie_totals = []
for calorie_group in calorie_groups:
    calorie_items = [int(calorie) for calorie in calorie_group.split('\n')]
    calorie_totals.append(sum(calorie_items))

############
## Part 1 ##
############

solution_1 = max(calorie_totals)
print(solution_1)

############
## Part 2 ##
############

calorie_totals.sort(reverse=True)
solution_2 = sum(calorie_totals[0:3])
print(solution_2)
