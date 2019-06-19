# Write nested for loops that produce the following output:

# 000111222333444555666777888999
# 000111222333444555666777888999
# 000111222333444555666777888999

for i in range(3):
    for j in range(10):
        for k in range(3):
            print (j, end = "")
    print("")