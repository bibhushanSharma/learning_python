# Write a program in a class named StarFigure that produces the following output using for loops.

# ////////////////\\\\\\\\\\\\\\\\
# ////////////********\\\\\\\\\\\\
# ////////****************\\\\\\\\
# ////************************\\\\
# ********************************

number_of_slashes = 16
number_of_stars = 0


for i in range(5):
    for j in range(number_of_slashes):
        print("/", end = "")
    for k in range(number_of_stars):
        print("*", end = "")
    for l in range(number_of_slashes):
        print("\\", end = "")
    number_of_slashes = number_of_slashes - 4
    number_of_stars = number_of_stars + 8
    print("")
