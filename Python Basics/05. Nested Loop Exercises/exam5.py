sea_tour = int(input()) # 680 лв.
mountain_tour = int(input()) # 499 лв.
sea_tour_price = 680
mountain_tour_price = 499
total = 0
sea_counter = 0
mountain_counter = 0
number_of_tours = sea_tour + mountain_tour

for _ in range(0, number_of_tours + 1):
    tour_name = input()

    if tour_name == "Stop":
        break
    elif tour_name == "sea" and sea_tour > 0:
        total += sea_tour_price
        sea_tour -= 1
        sea_counter +=1

    elif tour_name == "mountain" and mountain_tour > 0:
        total += mountain_tour_price
        mountain_tour -= 1
        mountain_counter += 1

if sea_tour < sea_counter and mountain_tour < mountain_counter:
    print("Good job! Everything is sold.")
    print(f"Profit: {total} leva.")
else:
    print(f"Profit: {total} leva.")
