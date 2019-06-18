# Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" 
# instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output : 
# fizzbuzz
# 1
# 2
# fizz
# 4 
# buzz
multiple_of_3 = "Fizz"
multiple_of_5 = "Buzz"
multiple_of_both = "FizBuzz"
for i in range(1,51):
    if i % 3 is 0 and i % 5 is 0:
        print(multiple_of_both)
    elif i % 3 is 0:
        print(multiple_of_3)
    elif i % 5 is 0:
        print(multiple_of_5)
    else:
        print (i)