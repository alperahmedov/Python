control_number = int(input())

count = 0
password = ""
pass_flag = False

for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if num1 < num2 and num3 > num4 and (num1 * num2 + num3 * num4) == control_number:

                    count += 1
                    print(f"{num1}{num2}{num3}{num4}", end=" ")

                    if count == 4:
                        pass_flag = True
                        password = str(num1) + str(num2) + str(num3) + str(num4)
print()

if pass_flag:
    print(f"Password: {password}")
else:
    print("No!")