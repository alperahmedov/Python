current_hour = int(input())
current_minute = int(input())
sum_time = (current_hour * 60) + current_minute + 15
hour = sum_time // 60
minutes = sum_time % 60
if hour > 23:
    print(f"0:{minutes:02d}")
else:
    print(f"{hour}:{minutes:02d}")
