number_of_unsatisfactory_grade = int(input())
average_score = 0
poor_grades = 0
last_problem = ""
problem_counter = 0
poor_grades_condition = False
while True:
    problem_name = input()
    if problem_name == "Enough":
        break
    grade = int(input())
    average_score += grade
    problem_counter += 1
    last_problem = problem_name

    if grade <= 4:
        poor_grades += 1

        if poor_grades == number_of_unsatisfactory_grade:
            poor_grades_condition = True
            break

average_score /= problem_counter
if poor_grades_condition:
    print(f"You need a break, {poor_grades} poor grades.")
else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problem_counter}")
    print(f"Last problem: {last_problem}")
