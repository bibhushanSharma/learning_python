# It's common to print a rotating, increasing list of single-digit numbers 
# at the start of a program's output as a visual guide to number the columns of the output to follow. 
# With this in mind, write nested for loops to produce the following output, with each line 60 characters wide:

#          |         |         |         |         |         |
# 123456789012345678901234567890123456789012345678901234567890
for k in range(6):
    for p in range(9):
        print(" ", end = "")
    print("/", end = "")
print("")
for i in range(6):
    for j in range(1,10):
        print(j, end = "")
    print("0", end = "")