number_of_students_in_exam = int(input())
top_students = 0
between_four_five = 0
between_three_four = 0
fail = 0
evalution_counter = 0
grade = 0
for _ in range(1, number_of_students_in_exam + 1):
    evalution = float(input())
    if evalution >= 5:
        top_students += 1
        grade += evalution
        evalution_counter += 1
    elif 4 <= evalution <= 4.99:
        between_four_five += 1
        grade += evalution
        evalution_counter += 1
    elif 3 <= evalution <= 3.99:
        between_three_four += 1
        grade += evalution
        evalution_counter += 1
    elif 3 > evalution:
        fail += 1
        grade += evalution
        evalution_counter += 1

average = grade / evalution_counter

percent_top = top_students / number_of_students_in_exam * 100
percent_four = between_four_five / number_of_students_in_exam * 100
percent_three = between_three_four / number_of_students_in_exam * 100
percent_fail =  fail / number_of_students_in_exam * 100


print(f"Top students: {percent_top:.2f}%")
print(f"Between 4.00 and 4.99: {percent_four:.2f}%")
print(f"Between 3.00 and 3.99: {percent_three:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {average:.2f}")

