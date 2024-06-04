# swapping

# a=5
# b=6
# print("numbers before swapping")
# print(a,b)

# c=a
# a=b
# b=c
# print("numbers after swapping")
# print(a,b)

#pos or neg

# a=int(input("enter a number:"))
# if a>0:
#     print("number is positive")
# else:
#     print("number is negative")

#leap year

# year=int(input("enter a year:"))
# a=year%4
# b=year%100
# c=year%400
# if a==0:
#     if b==0:
#         if c==0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")

#odd or even

# a=int(input("enter a number:"))
# if a%2==0:
#     print("even number")
# else:
#     print("odd number")

 
#fibonocci
 
# n=10
# x1=int(input("enter a number"))
# x2=x1
# while n<= n:
#     x3=x1+x2
# print()

#prime number

# n1=int(input("enter starting intervel:"))
# n2=int(input("enter ending intervel:"))
# for num in range(n1,n2+1):
#     if num>1:
#         for i in range(2,num):
#             if(num%i)==0:
#                 break                     
#         else:
#                 print(num)

        

# odd or even

# for i in range(1,50):
#     if(i%2)!=0:
#         print(i)
            

#factorial

# n=int(input("enter a number:"))
# f=1
# if n<0:
#     print("factorial is not defined")
# # elif n==0:
# #     print(f"factorial is of {n} is 1")
# else:
#     for i in range(1,n+1):
#         f*=i
# print(f"factorial of {n} is {f}")

#palindrome

# str1=input("enter a string:")
# str2=str1.replace(" ","")
# if str2==str2[::-1]:
#     print(f"{str1} is pallindrom")
# else:
#     print(f"{str1} is not pallindrom")

#sum of integers
# sum=0
# for i in range(101,200):
#     if i%7==0:
#      sum+=i   
# print(sum)
            
# multiplication table
# x=int(input("enter a number:"))
# y=1
# while x>1 and y<=10:
#     n=x*y

#     print(f"{x}*{y}={n}")
#     y+=1

#area and perimeter of rectangle

len=int(input("enter the length of the rectangle:"))
wid=int(input("enter the length of the rectangle:"))
area=len*wid
per=2*(len+wid)
print(f"area={area}")
print(f"perimeter={per}")

#armstrongnumber

n=int(input("enter a number:"))
num=str(n)
l=len(num)
sum=0
for x in num:
    sum+=int(x)**l
if sum==n:
    print("armstronge number")
else:
    print("not armstronge number")


