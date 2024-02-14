age = float(input())
gender = input()

if gender == "m":
    if age < 16:
        print("Master")
    if age >= 16:
        print("Mr.")
elif gender == "f":
    if age < 16:
        print("Miss")
    if age >= 16:
        print("Ms.")