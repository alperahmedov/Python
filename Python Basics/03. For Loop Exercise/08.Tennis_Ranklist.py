number_of_turnirs = int(input())
start_points = int(input())
points = 0
win_tournaments = 0
for _ in range(number_of_turnirs):
    final = input()

    if final == "W":
        points += 2000
        win_tournaments += 1
    if final == "F":
        points += 1200
    if final == "SF":
        points += 720

total_points = start_points + points
average_points = int(points / number_of_turnirs)
percentage = win_tournaments / number_of_turnirs * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percentage:.2f}%")
