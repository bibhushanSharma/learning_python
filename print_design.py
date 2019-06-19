# Write a method called printDesign that produces the following output. Use nested for loops to capture the 
# structure of the figure.

# -----1-----
# ----333----
# ---55555---
# --7777777--
# -999999999-

number = 1
number_of_dashes = 5
for d in range(5):
    for i in range(number_of_dashes):
        print("-", end = "")
    for k in range(number):
        print(number, end = "")
    for k in range(number_of_dashes):
        print ("-", end = "")
        
    print("")
    number = number + 2
    number_of_dashes = number_of_dashes - 1