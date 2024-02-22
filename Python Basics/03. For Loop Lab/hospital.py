period = int(input())
doctors = 7
no_doctor = 0
yes_doctor = 0

for day in range(1, period + 1):
    people_pacient = int(input())

    if day % 3 == 0 and no_doctor > yes_doctor:
        doctors += 1

    if people_pacient > doctors:
        no_doctor += people_pacient - doctors
        yes_doctor += doctors
    elif people_pacient <= doctors:
        yes_doctor += people_pacient


print(f"Treated patients: {yes_doctor}.")
print(f"Untreated patients: {no_doctor}.")

