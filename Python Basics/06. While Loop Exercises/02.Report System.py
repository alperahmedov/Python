target_sum = int(input())
bank_sum = 0
cash = 0
counter = 0
bank_counter = 0
cash_counter = 0
while True:
    price = input()
    counter += 1
    if price == "End":
        break
    int_price = int(price)
    if counter % 2 == 0 and 10 < int_price > 100:
        bank_sum += int_price
        bank_counter += 1
        print("Product sold!")

    elif counter % 2 != 0 and int_price <= 100:
        cash += int_price
        cash_counter += 1
        print("Product sold!")
    else:
        print("Error in transaction!")

    if bank_sum + cash >= target_sum:
        break
total_sum = bank_sum + cash
a_cash = cash / cash_counter
a_card = bank_sum / bank_counter

if total_sum >= target_sum:
    print(f"Average CS: {a_cash:.2f}")
    print(f"Average CC: {a_card:.2f}")
else:
    print("Failed to collect required money for charity.")
