# num = int(input("enter the number here: "))
# if num == 1:
#     print("it is not a prime number")
# if num>1:
#     for i in range(2,num):
#         if (num%i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")

# (RANDOM NUMBER)
# import random
# num=random.randint(1,15)
# print(num)
# (interval prime number)
# lower = int(input("enter lower limit here: "))
# upper = int(input("enter upper limit here: "))
# for num in range(lower, upper):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# (celsius to fehrenheit)
# celsius = int(input("enter temperature in celsius: "))
# fehrenheit = celsius*1.8+32
# print("the value in fehrenheit is ", fehrenheit)

# (FACTORIAL)
# num=int(input("enter a number here: "))
# fact=1
# if num<0:
#     print("factorial does not exist for negative numbers")
# if num==0:
#     print("factorial of 0 is 1")
# if num>0:
#     for i in range(1,num+1):
#         fact*=i
#     print("factorial of",num,"is",fact)
# (MULTPLICATION TABLE)
# n=int(input("enter a number here: "))
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)

# solution 2
# n=8
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i=i+1
# (FIBONNACI SERIES)
# a=0
# b=1
# num=int(input("enter a number to obtain a finonnaci sequence: "))
# if num==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(1,num): 
#         c=a+b
#         print(c)
#         a=b
#         b=c  
# (ARMSTRONG NUMBER)
# (SOLUTION 2)
lower=int(input("enter the lower limit here:"))
upper=int(input("enter the upper limit here:"))



for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print(num)
        
        
        

# (NATURAL NUMBER SUM)
# num=int(input("enter the number here:"))
# if num<0:
#     print("please enter a positive integer")
# else:
#     sum=0
#     while num>0:
#         sum+=num
#         num-=1
#     print(sum)
