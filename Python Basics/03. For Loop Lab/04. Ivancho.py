money =float(input())
year_life = int(input())
age = 18
sum = 0

for year in range(1800, year_life + 1):
    if year % 2 != 0:
        sum = sum + 12000 + (50 * age)
    elif year % 2 == 0:
        sum += 12000
    age += 1
    if money <= 0:
        break

diff = abs(money - sum)

if money >= sum:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")