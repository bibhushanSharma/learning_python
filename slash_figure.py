# Write a Java program in a class named SlashFigure that produces the following output. Use nested for loops to capture the structure of the figure. (If you previously solved Self-Check problems 34 and 35 in the book, you will have created a loop table that will be useful in solving this problem. Use it!)

# !!!!!!!!!!!!!!!!!!!!!!
# \\!!!!!!!!!!!!!!!!!!//
# \\\\!!!!!!!!!!!!!!////
# \\\\\\!!!!!!!!!!//////
# \\\\\\\\!!!!!!////////
# \\\\\\\\\\!!//////////
number_of_slashes = 0
number_of_exclamation_point = 22
for i in range (6):
    for k in range(number_of_slashes):
        print("\\", end = "")
    for j in range(number_of_exclamation_point):
        print("!", end = "")
    for l in range(number_of_slashes):
        print("/", end = "")
    print("")
    number_of_exclamation_point = number_of_exclamation_point - 4
    number_of_slashes+=2