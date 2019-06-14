# Write for loops to produce the following output:

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
number_one = 1
height_of_triangle = int(input("Enter height of triangle: "))
print(number_one)
for i in range(height_of_triangle - 1):
    number_one = number_one + 1
    for j in range(number_one):
        print(number_one, end= "")
    print("")
    