# Modify your code from the previous problem to produce the following output:

# 99999888887777766666555554444433333222221111100000
# 99999888887777766666555554444433333222221111100000
# 99999888887777766666555554444433333222221111100000
# 99999888887777766666555554444433333222221111100000
# 99999888887777766666555554444433333222221111100000

for i in range(5):
    for j in range(9, -1,-1):
        for k in range(5):
            print (j, end = "")
    print("")