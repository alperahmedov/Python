n = int(input())
left_sum = 0
right_sum = 0
for number in range (1, n+1):
    value = int(input())
    left_sum += value
for number in range (1, n+1):
    value = int(input())
    right_sum += value

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {diff}")





