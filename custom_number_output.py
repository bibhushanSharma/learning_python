# Modify your code from the previous exercise so that it could easily be modified to display a different
#  range of numbers (instead of 1234567890) and a different number of repetitions of those numbers 
# (instead of 60 total characters), with the vertical bars still matching up correctly. Write a complete 
# class named NumbersOutput. Use two class constants instead of "magic numbers,", with one constant set to 6
#  for the number of repetitions, and the other set to 10 for the range of numbers. Put the for loop code in 
# your class's main method.

# For example, if your number-of-repetitions constant is set to 7 and your range constant is set to 5, 
# the output should be the following:

#     |    |    |    |    |    |    |
# 12340123401234012340123401234012340
number_of_sets = int(input("How many sets do you want: "))
max_num = int(input("What would you like your maximun number to be? "))
for k in range(number_of_sets):
    for p in range(max_num):
        print(" ", end = "")
    print("/", end = "")
print("")
for i in range(number_of_sets):
    for j in range(1,max_num + 1):
        print(j, end = "")
    print("0", end = "")