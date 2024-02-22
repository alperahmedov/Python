capacity = float(input())
total = 0

while True:
    suitcase = input()
    if suitcase == "End" or suitcase == '':
        break

    if (total + 1) % 3 == 0:
        capacity -= float(suitcase) * 0.10

    capacity -= float(suitcase)

    if capacity <= 0:
        print("No more space!")
        break
    total += 1

if capacity > 0:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {total} suitcases loaded.")