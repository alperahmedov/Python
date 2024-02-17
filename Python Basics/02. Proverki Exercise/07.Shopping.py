budget = float(input())
videocards = int(input())
processors = int(input())
ram = int(input())

sum_videocards = videocards * 250
sum_processors = sum_videocards * 0.35
sum_ram = sum_videocards * 0.10

final_sum = sum_videocards + processors * sum_processors + ram * sum_ram


if videocards > processors:
    final_sum = final_sum - final_sum * 0.15

diff = abs(final_sum - budget)
if final_sum <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
