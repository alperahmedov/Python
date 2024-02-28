number_of_juri = int(input())
sum_grades = 0
grade_counter = 0
while True:
    problem_name = input()

    if problem_name == "Finish":
        average_sum = sum_grades / grade_counter
        print(f"Student's final assessment is {average_sum:.2f}.")
        break
    current_grade_counter = 0

    for x in range(number_of_juri):
        grade = float(input())
        grade_counter += 1
        sum_grades += grade
        current_grade_counter += grade
    current_average_grade = current_grade_counter / number_of_juri
    print(f"{problem_name} - {current_average_grade:.2f}.")
