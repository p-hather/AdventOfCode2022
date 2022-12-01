
with open('./01/input.txt') as file:
    calorie_input = file.read()

calorie_groups = calorie_input.split('\n\n')

calorie_totals = []
for calorie_group in calorie_groups:
    calorie_items = [int(calorie) for calorie in calorie_group.split('\n')]
    calorie_totals.append(sum(calorie_items))

solution_a = max(calorie_totals)
print(f'solution a is: {solution_a}')

calorie_totals.sort(reverse=True)
solution_b = sum(calorie_totals[0:3])
print(f'solution b is: {solution_b}')
