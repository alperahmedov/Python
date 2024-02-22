count_chiken = int(input())
count_fish = int(input())
count_vegan = int(input())
sum_chicken_menu = count_chiken * 10.35
sum_fish_menu = count_fish * 12.40
sum_vegan_menu = count_vegan * 8.15

total_sum_menu = sum_chicken_menu + sum_fish_menu + sum_vegan_menu
sum_desert = 0.2 * total_sum_menu

final_sum = total_sum_menu + sum_desert + 2.5
print(final_sum)