standard_ticket = 0
kid_ticket = 0
student_ticket = 0
# condition = False

movie = str(input())
while movie != "Finish":
    available_places = input()
    if available_places == "Finish":
        break
    available_places = int(available_places)
    current_ticket = 0
    for _ in range(1, available_places + 1):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "standard":
            standard_ticket += 1
            current_ticket += 1
        elif ticket_type == "kid":
            kid_ticket += 1
            current_ticket += 1
        elif ticket_type == "student":
            student_ticket += 1
            current_ticket += 1

    print(f"{movie} - {(current_ticket / available_places) * 100:.2f}% full.")
    movie = str(input())
if movie == "Finish":
    total_tickets = standard_ticket + student_ticket + kid_ticket
    print(f"Total tickets: {total_tickets}")
    print(f"{(student_ticket / total_tickets) * 100:.2f}% student tickets.")
    print(f"{(standard_ticket / total_tickets) * 100:.2f}% standard tickets.")
    print(f"{(kid_ticket / total_tickets) * 100:.2f}% kids tickets.")
