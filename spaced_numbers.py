# Write nested for loops to produce the following output:

#     1
#    2
#   3
#  4
# 5
number_of_spaces = 5
printed_number = 1
for i in range(5):
    for j in range(number_of_spaces):
        print(" ", end = "")
    print (printed_number)
    printed_number += 1
    number_of_spaces = number_of_spaces - 1