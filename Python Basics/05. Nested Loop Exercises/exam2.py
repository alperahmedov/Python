shirt_price = float(input())
golden_ball_sum = float(input())
short_price = shirt_price * 0.75
sock_price = short_price * 0.20
butonki_price = (shirt_price + short_price) * 2

total_sum = shirt_price + short_price + sock_price + butonki_price
total_sum = total_sum - total_sum * 0.15
diff = abs(total_sum - golden_ball_sum)
if total_sum > golden_ball_sum:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")

else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")
