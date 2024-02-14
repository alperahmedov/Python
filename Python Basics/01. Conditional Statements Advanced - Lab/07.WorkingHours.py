# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) - въведени от потребителя
# и проверява дали офисът на фирма е отворен, като работното време на офисът е от 10-18 часа, от понеделник до събота
# включително
hours = int(input())
day_of_week = input()

is_working_day = day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday" or day_of_week == "Saturday"

is_working_hour = 10 <= hours <= 18

if is_working_day and is_working_hour:
    print("open")
else:
    print("closed")
