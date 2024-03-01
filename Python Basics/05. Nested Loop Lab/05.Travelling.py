destination = input()
while destination != "End":
    need_money = float(input())
    available_money = 0
    while available_money < need_money:
        saved_money = float(input())
        available_money += saved_money
    else:
        print(f"Going to {destination}!")

    destination = input()