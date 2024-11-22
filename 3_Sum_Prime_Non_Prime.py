command = input()

prime_number_sum = 0
non_prime_numbers_sum = 0

while command != "stop":
    current_number = int(command)

    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue

    is_prime = True
    for i in range(2, current_number) :
        if current_number % i == 0 :
            is_prime = False
            break  # break out of the for loop since the number isn't prime


    if is_prime:
        prime_number_sum += current_number
    else:
        non_prime_numbers_sum += current_number

    command = input()
print(f"Sum of all prime numbers is: {prime_number_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")



