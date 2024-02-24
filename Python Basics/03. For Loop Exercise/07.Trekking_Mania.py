number_of_groups_climbers = int(input())
musala = 0
monblan = 0
kilamanjaro = 0
k2 = 0
everest = 0
counter_of_climbers = 0

for _ in range(number_of_groups_climbers):
    number_of_people_in_current_group = int(input())
    counter_of_climbers += number_of_people_in_current_group

    if number_of_people_in_current_group <= 5:
        musala += number_of_people_in_current_group
    elif 6 <= number_of_people_in_current_group <= 12:
        monblan += number_of_people_in_current_group
    elif 13 <= number_of_people_in_current_group <= 25:
        kilamanjaro += number_of_people_in_current_group
    elif 26 <= number_of_people_in_current_group <= 40:
        k2 += number_of_people_in_current_group
    elif number_of_people_in_current_group >= 41:
        everest += number_of_people_in_current_group

musala = musala / counter_of_climbers * 100
monblan = monblan / counter_of_climbers * 100
kilamanjaro = kilamanjaro / counter_of_climbers * 100
k2 = k2 / counter_of_climbers * 100
everest = everest / counter_of_climbers * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilamanjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")