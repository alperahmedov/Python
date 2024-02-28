days = int(input())
type_of_room = input()
evaluation = input()
nights = days - 1
sum = 0
if type_of_room == "room for one person":
    sum = nights * 18

elif type_of_room == "apartment":
    sum = nights * 25
    if nights < 10:
        sum = sum - 0.30 * sum
    elif 10 <= nights <= 15:
        sum = sum - 0.35 * sum
    elif nights > 15:
        sum = sum - 0.50 * sum
elif type_of_room == "president apartment":
    sum = nights * 35
    if nights < 10:
        sum = sum - 0.10 * sum
    elif 10 <= nights <= 15:
        sum = sum - 0.15 * sum
    elif nights > 15:
        sum = sum - 0.20 * sum
if evaluation == "positive":
    sum = sum + 0.25 * sum
elif evaluation == "negative":
    sum = sum - 0.10 * sum

print(f"{sum:.2f}")







