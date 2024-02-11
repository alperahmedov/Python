budget = float(input())
season = input()
fishermens = int(input())
rent_ship = 0

if season == "Spring":
    rent_ship = 3000
elif season == "Summer" or season == "Autumn":
    rent_ship = 4200
elif season == "Winter":
    rent_ship = 2600

if season in "Spring Summer Winter" and fishermens % 2 == 0:
    rent_ship -= rent_ship * 0.05

if fishermens <= 6:
    rent_ship -= rent_ship * 0.1
elif 7 <= fishermens <= 11:
    rent_ship -= rent_ship * 0.15
elif fishermens > 12:
    rent_ship -= rent_ship * 0.25

diff = abs(budget - rent_ship)
if budget >= rent_ship:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")

