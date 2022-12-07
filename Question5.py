### 5. Write a Python Program to Find Armstrong Number in an Interval?
##### Sol.

#Check length of number and decide power

lower = int(input("Enter lower value :- "))
upper = int(input("Enter higher value :- "))
print("From {} to {} following are the Armstrong Number:-".format(lower,upper))
for num in range(lower, upper + 1):
   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0
    #store sum in temperary storage
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num,end=' ')

###############################################
###############ANSWER#########################
#            Enter lower value :- 100
#            Enter higher value :- 1500
#            From 100 to 1500 following are the Armstrong Number:-
#            153 370 371 407
