name_of_student = input()
current_year_grade = 0
class_year = 1
average_grade = 0
failed_year = 0
grades_counter = 0

while class_year < 13:
    current_year_grade = float(input())
    if current_year_grade >= 4:
        class_year += 1
        grades_counter += current_year_grade
    else:
        failed_year += 1
        if failed_year > 1:
            break
average_grade = grades_counter / 12
if class_year == 13:
    print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{name_of_student} has been excluded at {class_year} grade")
