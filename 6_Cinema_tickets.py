total_tickets = 0
total_student = 0
total_standard = 0
total_kid = 0

command = input()
while command != "Finish":
    current_movie = command

    seats_available = int(input())
    # zapazvam kolko sa vsichki mesta(STATE)
    total_seats = seats_available

    ticket = input()
    while ticket != "End":
        if ticket == "student":
            total_student += 1
        elif ticket == "standard":
            total_standard += 1
        elif ticket == "kid":
            total_kid += 1

        seats_available -= 1
        if seats_available <= 0:
            break

        ticket = input()


    seats_bought = total_seats - seats_available
    percent_full = seats_bought / total_seats * 100
    print(f"{current_movie} - {percent_full:.2f}% full.")

    total_tickets += seats_bought

    command = input()

total_tickets = total_student + total_standard + total_kid

student_percent = total_student / total_tickets * 100
standard_percent = total_standard / total_tickets * 100
kid_percent = total_kid / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_percent :.2f}% student tickets.")
print(f"{standard_percent :.2f}% standard tickets.")
print(f"{kid_percent :.2f}% kids tickets.")
