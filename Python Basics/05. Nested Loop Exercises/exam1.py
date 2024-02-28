# Нощувка - 20 лв.
#  Карта за транспорт - 1.60 лв.
#  Билет за музей - 6 лв.

group_members = int(input())
nights_number = int(input())
number_of_bus_tickets = int(input())
number_of_museum_tickets = int(input())
night_price = 20
bus_price = 1.60
museum_price = 6

total_for_one_person = nights_number * night_price + (number_of_bus_tickets * bus_price) + (number_of_museum_tickets * museum_price)

sum = total_for_one_person * group_members
sum = sum + 0.25 * sum
print(f"{sum:.2f}")