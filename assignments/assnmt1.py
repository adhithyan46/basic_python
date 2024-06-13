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

#n=int(input("enter a number:"))


#armstronge

# n=int(input("enter a number:"))
# num=str(n)
# l=len(num)
# sum=0
# for x in num:
#     sum+=int(x)**l
# if sum==n:
#     print("armstronge number")
# else:
#     print("not armstronge number")

#remove puctuations

# str1=input("enter a string:")
# punch="'!@#$%^&*(){}[];:,.<>/?_-~`'"
# nopunch=""
# for c in str1:
#     if str not in punch:
#         nopunch+=c
# print("string with puctuation:",str1)
# print("string with no punctuations:",nopunch)

##prime number

#n1=int(input("enter starting intervel:"))
# n2=int(input("enter ending intervel:"))
# for num in range(n1,n2+1):
#     if num>1:
#         for i in range(2,num):
#             if(num%i)==0:
#                 break                     
#         else:
#                 print(num)


##odd or even

#odd or even

# for i in range(1,50):
#     if(i%2)!=0:
#         print(i)


##factorial

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

##palindrome

# str1=input("enter a string:")
# str2=str1.replace(" ","")
# if str2==str2[::-1]:
#     print(f"{str1} is pallindrom")
# else:
#     print(f"{str1} is not pallindrom")


##sum of integer

# sum=0
# for i in range(101,200):
#     if i%7==0:
#      sum+=i   
# print(sum)
            
## multiplication table

# x=int(input("enter a number:"))
# y=1
# while x>1 and y<=10:
#     n=x*y

#     print(f"{x}*{y}={n}")
#     y+=1

##area and perimeter of rectangle

# len=int(input("enter the length of the rectangle:"))
# wid=int(input("enter the length of the rectangle:"))
# area=len*wid
# per=2*(len+wid)
# print(f"area={area}")
# print(f"perimeter={per}")

# #largest amoung 3

# print("enter 3 numbers")
# a=float(input("enter 1st number:"))
# b=float(input("enter 2nd number:"))
# c=float(input("enter 3rd number:")) 
# if (a>c and a>b):
#     print(f"{a} is larger" )
# elif(b>c and b>a):
#     print(f"{b} 
#     is larger")
# else:
#     print(f"{c} is largest")

##armstronge number


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




#count vowels

# str1=input("enter a string:")
# vls=("a","e","i","o","u")
# ct_vls=0
# for i in str1:
#     if i in vls:
#         ct_vls+=1
# print(ct_vls)

#complex number

# c1=complex(input("enter 1st complex number:"))
# c2=complex(input("enter 2st complex number:"))
# print("addion:")
# add=c1+c2
# print(f"{c1}*{c2}={add}")
# print("substraction:")
# sub=c1-c2
# print(f"{c1}*{c2}={sub}")
# print("division:")
# div=c1/c2
# print(f"{c1}*{c2}={div}")
# print("multiplication:")
# mul=c1*c2
# print(f"{c1}*{c2}={mul}")

#

# num_1=10
# num_2=11
# print("num_1=10,num_2=11")
# num_3=num_1%num_2
# print(f"num_1%num_2={num_3}")
# num_3=num_1-num_2
# print(f"num_1-num_2={num_3}")
# num_3=num_1*num_2
# print(f"num_1*num_2={num_3}")


#

# num_1=7
# num_2=6
# print("num_1=7,num_2=6")
# num_3=num_1<num_2
# print(f"num_1<num_2={num_3}")
# num_3=num_1>num_2
# print(f"num_1>num_2={num_3}")
# num_3=num_1<=num_2
# print(f"num_1<=num_2={num_3}")
# num_3=num_1==num_2
# print(f"num_1=num_2={num_3}")

#

# num_1=3
# num_2=4
# print("num_1=3")
# print("num_2=4")
# num_3=(num_1<num_2)and(num_1!=num_2)
# print("(num_1<num_2)and(num_1!=num_2)=",num_3)
# num_3=(num_1>=num_2)or(num_1>num_2)
# print("(num_1>=num_2)or(num_1>num_2)=",num_3)
# num_3=not(num_1==num_2)
# print("not(num_1=num_2)",num_3)


#

# i=1
# while(i<6):
#     i=i+1
#     print(i)

#

# customer_num=5
# invoice_num=1212
# print("invoice No(s):")
# while(customer_num>0):
#     print("INV-",invoice_num)
#     invoice_num+=3
#     customer_num-=1


#

str1=input("enter a string:")
py="python"
ja=" java"
p=" php"
if len(str1)>=5:
    if py in str1:
       str1+=ja
       print(str1)
    elif py not in str1:
        str1+=py
        print(str1)
else:
    str1+=p
    print(str1)

