# Входни данни -
# бр. химикали (int), бр. маркери (int), литри препарат (int)
# сума за химикали = бр. химикали * 5.80
# сума за маркери = бр. маркери * 7.20
# сума за препарата = бр. литри преп. * 1.2
# обща сума = сума за препарати + сума химикали + сума маркери
# отстъпка
# отпечатване крайна сума след отстъпката
count_pens = int(input())
count_markers = int(input())
liters_cleaner = int(input())
percent = int(input())
sum_pens = count_pens * 5.80
sum_markers = count_markers * 7.20
sum_cleaner = liters_cleaner * 1.20
all_sum = sum_pens + sum_markers + sum_cleaner
all_sum = all_sum - (all_sum * (percent / 100))
print(all_sum)




