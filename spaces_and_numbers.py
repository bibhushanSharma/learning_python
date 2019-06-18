# Write nested for loops to produce the following output:

#     1
#    22
#   333
#  4444
# 55555

for i in range(1,6):
    for j in range(-i+6):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    print("")