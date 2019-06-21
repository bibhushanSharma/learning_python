# Write a Java program called DollarFigure that produces the following output. Use nested for loops to capture the structure of the figure.

# $$$$$$$**************$$$$$$$
# **$$$$$$************$$$$$$**
# ****$$$$$**********$$$$$****
# ******$$$$********$$$$******
# ********$$$******$$$********
# **********$$****$$**********
# ************$**$************

number_of_outer_star = 0
number_of_inner_star = 14
number_of_dollar_sign = 7

for i in range(7):
    for k in range(number_of_outer_star):
        print("*", end = "")
    for j in range(number_of_dollar_sign):
        print("$", end = "")
    for l in range(number_of_inner_star):
        print("*", end = "")
    for p in range(number_of_dollar_sign):
        print("$", end = "")
    for w in range(number_of_outer_star):
        print("*", end = "")
    number_of_dollar_sign = number_of_dollar_sign - 1
    number_of_outer_star = number_of_outer_star + 2
    number_of_inner_star = number_of_inner_star - 2
    print("")
