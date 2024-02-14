#Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя и принтира на конзолата цената на билет за кино според деня от седмицата:
#Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday

day_of_week = input()

if day_of_week == "Monday"	or day_of_week == "Tuesday" or day_of_week == "Friday":
    print(12)
elif day_of_week == "Wednesday" or day_of_week == "Thursday":
    print(14)
elif day_of_week == "Saturday"	or day_of_week == "Sunday":
    print(16)
