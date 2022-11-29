### 2. Write a Python Program to Display the multiplication Table?
##### Sol.

#taking input from user
num=int(input("Enter number : "))

for i in range (1,11):
    mul=num*i
    #printing output value in multiplaction
    print("{} * {} = {}".format(num,i,mul))


###############################################
###############ANSWER#########################
#                Enter number : 7
#                7 * 1 = 7
#                7 * 2 = 14
#                7 * 3 = 21
#                7 * 4 = 28
#                7 * 5 = 35
#                7 * 6 = 42
#                7 * 7 = 49
#               7 * 8 = 56
#                7 * 9 = 63
#                7 * 10 = 70