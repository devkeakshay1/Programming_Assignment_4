### 4. Write a Python Program to Check Armstrong Number?
##### Sol.

num=input("Enter number :- ");
sum=0
#Check length of number and decide power
length=len(str(num))

for i in num:
    sum=int(i)**length+sum
    i=+1;

if int(num)==sum:
    print("{{} is Armstrong Number.".format(num))
else:
    print("{} is not an Armstrong Number.".format(num))

###############################################
###############ANSWER#########################
#            Enter number :- 153
#            153 is Armstrong Number.

#            Enter number :- 1221
#            1221 is not an Armstrong Number.
