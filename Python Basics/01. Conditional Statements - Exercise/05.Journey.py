budget = float(input())
season = input()
costs = 0

if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        costs = budget * 0.30
        print(f"Camp - {costs:.2f}")
    elif season == "winter":
        costs = budget * 0.7
        print(f"Hotel - {costs:.2f}")

elif 100 < budget <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        costs = budget * 0.4
        print(f"Camp - {costs:.2f}")
    elif season == "winter":
        costs = budget * 0.8
        print(f"Hotel - {costs:.2f}")

elif budget > 1000:
    print("Somewhere in Europe")
    costs = budget * 0.90
    print(f"Hotel - {costs:.2f}")

