length_of_sequense = int(input("How long do you want to sequence to be? "))
first_number = 0
print(first_number)
second_number = 1
print(second_number)

for _ in range(length_of_sequense - 2):
    current_number = first_number + second_number
    print(current_number)
    first_number = second_number
    second_number = current_number
