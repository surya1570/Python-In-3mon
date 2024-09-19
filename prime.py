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
# lower=int(input("enter the lower limit here:"))
# upper=int(input("enter the upper limit here:"))



# for num in range(lower,upper+1):
#     order=len(str(num))
#     sum=0
#     temp=num
#     while temp>0:
#         digit=temp%10
#         sum+=digit**order
#         temp//=10
#     if num==sum:
#         print(num)
        
        
        

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

# (POWER Anonymous Function)
# nterms = int(input("enter the number of terms here:"))
# result =list(map (lambda x:2**x,range(nterms+1)))
# print(result)
# for i in range(nterms+1):
#     print("the value of 2 raised to power",i," is",result[i])

# (Numbers Divisible by Another Number)
# print ("the number divisible by 13 are:")
# for i in range(1,100):
#     if i%13==0:
#         print(i)
        
# (SOLUTION 2 lamda function)
# l=[39,130,75,100,88,76]
# result=list(filter(lambda x:x%13==0,l))
# print("the number divisible by 13 are",result)

# (conversion of decimal)
# decimal=int(input("enter a number here:"))
# print("the conversion of decimal number",decimal,"is:")
# print(bin(decimal),"in binary")
# print(oct(decimal),"in octal")
# print(hex(decimal),"in hexal")
# (ASCII VALUE)

# char="a"
# print("the ascii value of ",char,"is",ord(char))
# 
# (hcf&gcd)
# def findhcf(x,y):
#  if x>y:
#   smaller=y
#  else:
#     smaller=x  
#  for i in range(1,smaller+1):
#         if((x%i==0)and(y%i==0)):
#             hcf=i
#  return hcf
# print("the hcf of the given two number is ",findhcf(12,45))
        
    
# (FACTOR)
# num=int(input("enter a number here"))
# for i in range(1,num+1):
#  if num%i==0:
#      print(i)
    
# (SIMPLE CALCULATOR)
# num1=float(input("enter a first number here"))
# num2=float(input("enter a second number here"))
# print("press 1 for addition\npress 2 for multiplication\npress 3 for division\npress 4 for subtraction")
# choice=int(input("enter your choice from 1-4:"))
# if choice==1:
#     print(num1+num2)
# elif choice==2:
#     print(num1*num2)
# elif choice==3:
#     print(num1/num2)
# elif choice==4:
#     print(num1-num2)
# else: 
#     print("invalid number")

# (shuffle Deck of Cards)
# ?

# (CALENDER)

# import calendar

# year=int(input("enter the year:"))
# month=int(input("enter the month:"))
# calendar=calendar.month(year,month)
# print(calendar)

# (FOBINNACI SEQUENCE)
# def fibo(n):
#     if n<=1:
#      return n
#     else:
#      return fibo (n-1)+fibo(n-2)
# n=int(input("enter the number here: "))
# if n<=0:
#      print("enter a positive number")
# else:
#      print("fibonacci sequence")
#      for i in range(n):
#       print(fibo(i))

# (SUM BY RECURSION METHOD)
# def nns(n):
#   if n<=1:
#      return n
#   else:
#      return (n)+nns(n-1)
# n=int(input("enter the number here: "))
# if n<=0:
#      print("enter a positive number")
# else:
#      print("the sum of natural numbers upto given number is ",nns(n))

# (factorial in recursion method)
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return (n*fact(n-1))
# n=int(input("enter the number here: "))
# if n<=0:
#     print("factorial of number less 1 does not exist")
# else:
#     print("factorial of given number is",fact(n))
    
#  (convert decimal in recursion method)
# # def convertbinary(n):
#    if n>1:
#        convertbinary(n//2)
#        print(n%2)
# convertbinary(20)

# (add two matrix numbers)
# A=[[1,2,3,],
#   [4,5,6],
#   [7,8,9]]
# B=[[1,2,3,],
#    [4,5,6],
#    [7,8,9]]

# result=[[0,0,0],
#         [0,0,0],
#         [0,0,0]]

# for i in range(len(A)):
#     for j in range(len(B)):
#          result[i][j]=A[i][j]+B[i][j]
# for r in result:
#  print(r)
# 
# (TRANSPOSE MATRIX)

# A=[[1,2,3,],
#     [4,5,6],
#     [7,8,9]]
# T=[[0,0,0],
#     [0,0,0],
#     [0,0,0]]

# for i in range(len(A)):
#   for j in range (len(A[0])):
#     T[j][i]=A[i][j]
    
# for i in T:
#       print(i)

# (PALINDROME STRING)
# a=input("enter a word here:")
# rev=a[::-1]
# if a==rev:
#   print("it is a palindrome ")
# else:
#   print("it is not a palindrome ")

# (PUNCTUATION)
# punc=''"!@#$%^&*()\?.~"''
# string=input("Enter anything here: ")
# empty_str=""
# for i in string:
#   if i not in punc:
#     empty_str+=i
# print(empty_str)

# (MATRIX MULTPLICATION)

# A=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]

# B=[[9,8,7,8],
#    [6,5,4,3],
#    [3,2,1,6]]
# result=[[0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0]]
# for i in range(len(A)):
#   for j in range(len(B[0])):
#     for k in range(len(B)):
#       result[i][j]+=A[i][k]* B[k][j]
# for i in result:
#     print(i)
   
  #  (ALPHABETIC ORDER)
  
# a=input("Enter something here:")
# w=a.split()
# print(w)
# for i in range(len(w)):
#   w[i]=w[i].lower()
# print(w)
# w.sort()
# print(w)

# (SET OPERATION)
A={1,7,9,5,3}
B={1,2,6,8,9}
print("the union is ",A|B)
print("the intersection is",A&B)
print("the differernce is",A-B)
print("the symmetric is",A^B)