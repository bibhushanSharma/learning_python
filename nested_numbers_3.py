# Modify your code from the previous problem to produce the following output:

# 999999999888888887777777666666555554444333221
# 999999999888888887777777666666555554444333221
# 999999999888888887777777666666555554444333221
# 999999999888888887777777666666555554444333221

for i in range(4):
    for j in range(9, 0, -1):
        for k in range(j):
            print (j, end = "")
    print("")