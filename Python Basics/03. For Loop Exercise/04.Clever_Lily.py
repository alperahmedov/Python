age_of_lily = int(input())
washing_mashine = float(input())
price_toy = int(input())
number_of_toys = 0
saved_money = 0

for num in range(1, age_of_lily + 1):

    if num % 2 == 0:
        saved_money += ((num / 2) * 10) - 1

    else:
        number_of_toys += 1

total_money = saved_money + (number_of_toys * price_toy)
diff = abs(total_money-washing_mashine)
if total_money >= washing_mashine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


