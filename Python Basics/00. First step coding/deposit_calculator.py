# Входни данни
deposit_sum = float(input())
months = int(input())
percent = float(input())

final_sum = deposit_sum + months * ((deposit_sum * (percent / 100)) / 12)
print(final_sum)




