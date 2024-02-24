name_actor = input()
start_points_from_academy = float(input())
number_of_juri = int(input())
points = 0
for _ in range(1, number_of_juri + 1):
    name_of_juri = input()
    points_from_juri = float(input())
    points += (len(name_of_juri) * points_from_juri) / 2
    total_points = points + start_points_from_academy
    diff = abs(1250.5 - total_points)
    if total_points > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")

