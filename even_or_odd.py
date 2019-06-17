odd_count = 0
even_count = 0
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(odd_count)
print(even_count)