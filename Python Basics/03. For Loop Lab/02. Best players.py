import sys

player = ""
hat_trick = 0
best_player = ""
max_goal = -sys.maxsize
while True:
    player = input()
    if player == "END":
        break
    total_goals = int(input())
    if total_goals > max_goal:
        max_goal = total_goals
        best_player = player

    if total_goals >= 10:
        break
print(f"{best_player} is the best player!")
if max_goal >= 3:
    print(f"He has scored {max_goal} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goal} goals.")
