n = int(input())
current_number = 1
condition = False

for row in range(1, n + 1):
    for col in range(1, row + 1):

        if current_number > n:
            condition = True
            break
        print(current_number, end = " ")
        current_number += 1

        if condition:
            break
    print()