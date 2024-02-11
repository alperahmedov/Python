screening_type = input()
rows = int(input())
columns = int(input())

all_places = rows * columns

if screening_type == "Premiere":
    profits = all_places * 12

if screening_type == "Normal":
    profits = all_places * 7.5

if screening_type == "Discount":
    profits = all_places * 5

print(f"{profits:.2f} leva")


