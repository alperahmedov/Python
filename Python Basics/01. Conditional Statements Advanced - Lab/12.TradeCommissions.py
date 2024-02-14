town = input()
sales = float(input())
commission = 0

if 0 <= sales <= 500 and town == "Sofia":
    commission = sales * 0.05
elif 500 < sales <= 1000 and town == "Sofia":
    commission = sales * 0.07
elif 1000 < sales <= 10000 and town == "Sofia":
    commission = sales * 0.08
elif sales > 10000 and town == "Sofia":
    commission = sales * 0.12

if 0 <= sales <= 500 and town == "Varna":
    commission = sales * 0.045
elif 500 < sales <= 1000 and town == "Varna":
    commission = sales * 0.075
elif 1000 < sales <= 10000 and town == "Varna":
    commission = sales * 0.1
elif sales > 10000 and town == "Varna":
    commission = sales * 0.13

if 0 <= sales <= 500 and town == "Plovdiv":
    commission = sales * 0.055
elif 500 < sales <= 1000 and town == "Plovdiv":
    commission = sales * 0.08
elif 1000 < sales <= 10000 and town == "Plovdiv":
    commission = sales * 0.12
elif sales > 10000 and town == "Plovdiv":
    commission = sales * 0.145
if commission > 0:
    print(f"{commission:.2f}")
else:
    print("error")
