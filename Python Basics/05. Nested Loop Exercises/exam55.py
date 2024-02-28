numbers_for_sea = int(input())
numbers_for_mountain = int(input())
command = ""
left_for_sea = numbers_for_sea
left_for_mountain = numbers_for_mountain
total_sum_sea = 0
total_sum_mountain = 0
while command != "Stop":
    command = input()
    if command == "sea":
        left_for_sea -= 1
        if left_for_sea >= 0:
            total_sum_sea += 680

    elif command == "mountain":
        left_for_mountain -= 1
        if left_for_mountain >= 0:
            total_sum_mountain += 499

    if left_for_sea <= 0 and left_for_mountain <= 0:
        print("Good job! Everything is sold.")
        print(F"Profit: {total_sum_sea + total_sum_mountain} leva.")
        break

else:
    print(F"Profit: {total_sum_sea + total_sum_mountain} leva.")
