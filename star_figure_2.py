# Modify your StarFigure code from the previous problem to use a constant for the size. 
# The outputs below use a constant size of 3 (left) and 6 (right):

# size 3	
# ////////\\\\\\\\
# ////********\\\\
# ****************
# size 6
# ////////////////////\\\\\\\\\\\\\\\\\\\\
# ////////////////********\\\\\\\\\\\\\\\\
# ////////////****************\\\\\\\\\\\\
# ////////************************\\\\\\\\
# ////********************************\\\\
# ****************************************



height_1 = 3
height_2 = 6
number_of_slashes_1 = (height_1 * 2) + 2
number_of_slashes_2 = (height_2 * 3) + 2
number_of_stars = 0


for i in range(height_1):
    for j in range(number_of_slashes_1):
        print("/", end = "")
    for k in range(number_of_stars):
        print("*", end = "")
    for l in range(number_of_slashes_1):
        print("\\", end = "")
    number_of_slashes_1 = number_of_slashes_1 - 4
    number_of_stars = number_of_stars + 8
    print("")
number_of_stars = 0
for i in range(height_2):
    for j in range(number_of_slashes_2):
        print("/", end = "")
    for k in range(number_of_stars):
        print("*", end = "")
    for l in range(number_of_slashes_2):
        print("\\", end = "")
    number_of_slashes_2 = number_of_slashes_2 - 4
    number_of_stars = number_of_stars + 8
    print("")


