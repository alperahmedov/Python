total_gold = 0
location_counter = 0
location = int(input())
for loc in range(1, location + 1):
    expected_gold = float(input())
    days_of_work = int(input())
    for day in range(1, days_of_work + 1):
        gold_per_day = float(input())
        total_gold += gold_per_day

    average_gold = total_gold / days_of_work
    diff = abs(average_gold - expected_gold)
    total_gold = 0
    if average_gold >= expected_gold:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    elif average_gold < expected_gold:
        print(f"You need {diff:.2f} gold.")
