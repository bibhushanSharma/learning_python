def one_number(split_number):
    if split_number[0] == "0":
        print(" ")
    elif split_number[0] == "1":
        print("I")
    elif split_number[0] == "2":
        print("II")
    elif split_number[0] == "3":
        print("III")
    elif split_number[0] == "4":
        print("IV")
    elif split_number[0] == "5":
        print("V")
    elif split_number[0] == "6":
        print("VI")
    elif split_number[0] == "7":
        print("VII")
    elif split_number[0] == "8":
        print("VIII")
    elif split_number[0] == "9":
        print("IX")
    else:
        print("Invalid input")

def two_number(first, second):
    if first == "0":
        print("", end = "")
    elif first == "1":
        print("X", end = "")
    elif first == "2":
        print("XX", end = "")
    elif first == "3":
        print("XXX", end = "")
    elif first == "4":
        print("XL", end = "")
    elif first == "5":
        print("L", end = "")
    elif first == "6":
        print("LX", end = "")
    elif first == "7":
        print("LXX", end = "")
    elif first == "8":
        print("LXXX", end = "")
    elif first == "9":
        print("XC", end = "")
    one_number(second)

number = input("Enter a number between 1 and 99: ")
split_number = list(number)
if len(split_number) is 1:
    one_number(split_number[0])
elif len(split_number) is 2:
    two_number(split_number[0], split_number[1])
else:
    print("Indalid input")



