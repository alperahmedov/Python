import sys

goals_max = -sys.maxsize
best_player = ""
goals = 0
while True:
    name = str(input())
    if name == "END":
        break
    goals = int(input())
    if goals > goals_max:
        goals_max = goals
        best_player = name
    if goals >= 10:
        break
print(f"{best_player} is the best player!")
if goals >= 3:
    print(f"He has scored {goals_max} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals_max} goals.")
