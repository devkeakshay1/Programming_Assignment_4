### 3. Write a Python Program to Print the Fibonacci sequence?
##### Sol.jkkl


#The Fibonacci sequence is a set of integers (the Fibonacci numbers) that 
# starts with a zero, followed by a one, then by another one, 
# and then by a series of steadily increasing numbers. 
# The sequence follows the rule that each number is equal to 
# the sum of the preceding two numbers.

num_1=0;
num_2=1;
count=0;
num=int(input("enter length :- "))

if num<=0:
    print("Print positive number")
elif num==1:
    print(num_1)
else:
    print("The Fibonacci sequence is :- ")
    print(num_1,end=' ')
    print(num_2,end=' ')
    while num-2>count:
        p=num_1+num_2
        print(p,end=' ')
        num_1=num_2
        num_2=p
        count+=1;

###############################################
###############ANSWER#########################
#         enter length :- 11
#         The Fibonacci sequence is :- 
#         0 1 1 2 3 5 8 13 21 34 55 

