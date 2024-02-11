month = input()
number_of_night = int(input())
studio_price = 0
apartment_price = 0

if month in "May October":
    studio_price = 50
    apartment_price = 65
    if 7 < number_of_night <= 14:
        studio_price -= studio_price * 0.05
    elif number_of_night > 14:
        studio_price -= studio_price * 0.3
elif month in "June September":
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_night > 14:
        studio_price -= studio_price * 0.20
elif month in "July August":
    studio_price = 76
    apartment_price = 77

if number_of_night > 14:
    apartment_price -= apartment_price * 0.10

a_price = apartment_price * number_of_night
s_price = studio_price * number_of_night

print(f"Apartment: {a_price:.2f} lv.")
print(f"Studio: {s_price:.2f} lv.")
