zekat_money = float(input())
nisab = 6600

if zekat_money >= nisab:
    zekat = zekat_money * 0.025
else:
    print("No zekat for this money")