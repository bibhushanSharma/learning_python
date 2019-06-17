user_input = input("Enter A Message: ")
number_of_numbers = 0
number_of_letters = 0
for character in user_input:
    if character.isdigit():
        number_of_numbers+=1
    elif character.isalpha():
        number_of_letters+=1
    else:
        pass
print(str(number_of_numbers) + " numbers")
print(str(number_of_letters) + " letters")