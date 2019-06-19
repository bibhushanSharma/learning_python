# Modify the SlashFigure program from the previous exercise to produce a new program SlashFigure2 that 
# uses a global constant for the figure's height. The previous output used a constant height of 6. 
# Here is the outputs for a constant height of 4 and 7 respectively: (If you previously solved Self-Check 
# problems 34 and 35 in the book, you will have created a loop table that will be useful in solving this problem.
# Use it!)

# size 4	
# !!!!!!!!!!!!!!
# \\!!!!!!!!!!//
# \\\\!!!!!!////
# \\\\\\!!//////
# size 7
# !!!!!!!!!!!!!!!!!!!!!!!!!!
# \\!!!!!!!!!!!!!!!!!!!!!!//
# \\\\!!!!!!!!!!!!!!!!!!////
# \\\\\\!!!!!!!!!!!!!!//////
# \\\\\\\\!!!!!!!!!!////////
# \\\\\\\\\\!!!!!!//////////
# \\\\\\\\\\\\!!////////////
height_1 = 4
height_2 = 7
number_of_slashes_1 = 0
number_of_slashes_2 = 0
number_of_exclamation_point_1 = (height_1 * 4) - 2
number_of_exclamation_point_2 = (height_2 * 4) - 2
for i in range (height_1):
    for k in range(number_of_slashes_1):
        print("\\", end = "")
    for j in range(number_of_exclamation_point_1):
        print("!", end = "")
    for l in range(number_of_slashes_1):
        print("/", end = "")
    print("")
    number_of_exclamation_point_1 = number_of_exclamation_point_1 - 4
    number_of_slashes_1+=2
print("")
for i in range (height_2):
    for k in range(number_of_slashes_2):
        print("\\", end = "")
    for j in range(number_of_exclamation_point_2):
        print("!", end = "")
    for l in range(number_of_slashes_2):
        print("/", end = "")
    print("")
    number_of_exclamation_point_2 = number_of_exclamation_point_2 - 4
    number_of_slashes_2+=2
