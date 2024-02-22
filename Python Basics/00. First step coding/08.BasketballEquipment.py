tax_per_year = int(input())
price_trainers = tax_per_year - 0.4 * tax_per_year
price_suit = price_trainers - 0.2 * price_trainers
price_ball = price_suit / 4
price_acc = price_ball / 5

expenses = tax_per_year + price_trainers + price_suit + price_ball + price_acc

print(expenses)