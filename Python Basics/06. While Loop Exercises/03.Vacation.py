vacantion_price = float(input())
available_money = float(input())
spend_counter = 0
day_counter = 0
while True:
    operation = input()
    current_sum = float(input())
    day_counter += 1

    if operation == "spend":
        spend_counter += 1

        if available_money - current_sum < 0:
            available_money = 0
        else:
            available_money -= current_sum

        if spend_counter == 5:
            break

    elif operation == "save":
        available_money += current_sum
        spend_counter = 0
        if available_money >= vacantion_price:
            break

if spend_counter < 5:
    print(f"You saved the money for {day_counter} days.")

else:
    print(f"You can't save the money.")
    print(f"{day_counter}")

