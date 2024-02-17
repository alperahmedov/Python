time_a = int(input())
time_b = int(input())
time_c = int(input())

sum_times = time_a + time_b + time_c
minutes = sum_times // 60
seconds = sum_times % 60
#if seconds < 10:
   # print(f"{minutes}:0{seconds}")
#else:
   # print(f"{minutes}:{seconds}")

print(f"{minutes}:{seconds:02d}")