type_of_flowers = input()
number = int(input())
budget = int(input())
costs = 0

if type_of_flowers == "Roses":
    costs = number * 5
    if number > 80:
        costs -= costs * 0.1
elif type_of_flowers == "Dahlias":
    costs = number * 3.80
    if number > 90:
        costs -= costs * 0.15
elif type_of_flowers == "Tulips":
    costs = number * 2.80
    if number > 80:
        costs -= costs * 0.15

elif type_of_flowers == "Narcissus":
    costs = number * 3
    if number < 120:
        costs += costs * 0.15

elif type_of_flowers == "Gladiolus":
    costs = number * 2.50
    if number < 80:
        costs += costs * 0.2

diff = abs(budget-costs)
if budget >= costs:
    print(f"Hey, you have a great garden with {number} {type_of_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")


