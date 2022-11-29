### 1. Write a Python Program to Find the Factorial of a Number?
##### Sol.

#Taking input from user
num=int(input("Enter number : "))
Factorial=1
#Usng for loop for taking value one by one upto input value
for i in range (1,num):
    #multiple number in range one by one 
    num=num*i
    Factorial=num
print("Factorial is {}".format(Factorial))

############################################
##############ANSWER########################
#
#          Enter number : 5
#           Factorial is 120
