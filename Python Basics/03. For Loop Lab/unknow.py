days = int(input())
hours = int(input())

total_amount = 0

for payment_days in range(1, days + 1):
    daily_amount = 0
    for payment_hours in range(1, hours + 1):

        if payment_days % 2 == 0 and payment_hours % 2 != 0:
            daily_amount += 2.5
        elif payment_days % 2 != 0 and payment_hours % 2 == 0:
            daily_amount += 1.25
        else:
            daily_amount += 1

    print(f"Day: {payment_days} - {daily_amount:.2f} leva")
    total_amount += daily_amount

print(f"Total: {total_amount:.2f} leva")