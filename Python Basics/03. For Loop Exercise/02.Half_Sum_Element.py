import sys

number = int(input())
max_num = -sys.maxsize
total_sum = 0
for _ in range(number):
     current_number = int(input())

     if current_number > max_num:
        max_num = current_number
     total_sum += current_number


if total_sum - max_num == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - (total_sum - max_num))
    print("No")
    print(f"Diff = {diff}")


