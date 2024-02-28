special_number = int(input())

for first_number in range(1,10):
    for second_number in range(1, 10):
        for thirth_number in range(1, 10):
            for forth_number in range(1, 10):

                if special_number % first_number == 0 and special_number % second_number == 0 and special_number % thirth_number ==0 \
                        and special_number % forth_number ==0:
                    print(f"{first_number}{second_number}{thirth_number}{forth_number}", end= " ")
