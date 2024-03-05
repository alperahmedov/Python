width = int(input())
lenght = int(input())
high = int(input())
home_volume = width * lenght * high
carton_volume = 1
all_cartons_volume = 0


while True:
    current_number_of_cartons = input()
    if current_number_of_cartons == "Done":
        break
    carton_space = carton_volume * int(current_number_of_cartons)
    all_cartons_volume += carton_space

    if home_volume < all_cartons_volume:
        break

diff = abs(home_volume - all_cartons_volume)

if home_volume < all_cartons_volume:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")
