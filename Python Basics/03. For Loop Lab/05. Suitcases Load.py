capacity = float(input())
suitcase_total = 0


while True:
    suitcase = input()
    if suitcase == "End":
        break
    suitcase_total += 1
    if suitcase_total % 3 == 0:
        suitcase = float(suitcase) + 0.10 * float(suitcase)
    capacity -= float(suitcase)

    if capacity <= 0:
        suitcase_total -= 1
        print("No more space!")
        break
if capacity > 0:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {suitcase_total} suitcases loaded.")
