# Write for loops to produce the following output, with each line 40 characters wide:

# ----------------------------------------
# _-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-
# 1122334455667788990011223344556677889900
# ----------------------------------------
for i in range(40):
    print("-", end = "")
print("")
for k in range(8):
    print("_-^- ", end = "")
print("")
for j in range(2):
    num = 1
    for o in range(9):
        print(str(num) + str(num), end = "")
        num +=1
    print("00", end = "")
print("")
for i in range(40):
    print("-", end = "")