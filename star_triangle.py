# Write for loops to produce the following output:

# *
# **
# ***
# ****
# *****
height_of_triangle = int(input("Enter height of triangle: "))
star = "*"
for i in range(1):
    for j in range(height_of_triangle):
        print(star)
        star = star + "*"