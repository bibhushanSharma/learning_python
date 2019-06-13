# Write for loops to produce the following output:
# *****
# *****
# *****
# *****
width = int(input("Width of Rectangle: "))
height = int(input("Height of Rectangle: "))
for _ in range(height):
    for __ in range(width):
        print("*", end="") 
    print("")