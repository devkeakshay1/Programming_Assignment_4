### 6. Write a Python Program to Find the Sum of Natural Numbers?
##### Sol.

#Natural numbers are a part of the number system, including all the positive 
# numbers from 1 to infinity. Natural numbers are also called counting numbers 
# because they do not include zero or negative numbers. They are a part of real 
# numbers including only the positive integers, but not zero, fractions, 
# decimals, and negative numbers.

num=int(input("Enter a positive number:- "))
sum=0
for i in range(0,num+1):
    sum=i+sum
    i=+1
print("Sum of {} natural number is {}".format(num,sum))

###############################################
###############ANSWER#########################
#        Enter a positive number:- 100
#        Sum of 100 natural number is 5050