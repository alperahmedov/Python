number = input()

for num1 in range(1, int(number[2]) + 1):
    for num2 in range(1, int(number[1]) + 1):
        for num3 in range(1, int(number[0])+ 1):
            result = num1 * num2 * num3
            print (f"{num1} * {num2} * {num3} = {result};")
