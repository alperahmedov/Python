number = int(input())
if number <= 100:
    bonus_points = 5
elif 100 < number <= 1000:
    bonus_points = number * 0.2
elif number > 1000:
    bonus_points = number * 0.1
if number % 10 == 5:
    bonus_points += 2
elif number % 2 == 0:
    bonus_points += 1
all_points = bonus_points + number
print(bonus_points)
print(all_points)
