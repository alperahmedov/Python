flag = False
prime = 0
non_prime = 0

while True:
    current_number = input()

    if current_number == "stop":
        break
    current_number = int(current_number)

    if current_number < 0:
        print("Number is negative.")

    else:
        if current_number > 1:
            for i in range(2, current_number):
                if current_number % i == 0:
                    flag = True
                    break

            if flag:
                non_prime += current_number
                flag = False
            else:
                prime += current_number

print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")