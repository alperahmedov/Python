from math import ceil

serial_name = input()
serial_time = int(input())
breake_time = int(input())

time_for_lunch = breake_time * 1/8
rest_time = breake_time * 1/4
left_time = breake_time - time_for_lunch - rest_time
diff = abs(left_time - serial_time)
if left_time >= serial_time:
    print(f"You have enough time to watch {serial_name} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(diff)} more minutes.")