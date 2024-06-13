#if

# n=10
# if n > 0:
#     print("positive")

#if else

# n=int(input("enter a number:"))
# if n>0:
#     print("number is positive")
# else:
#     print("number is negative")

#if elif else

# n=int(input("enter a number:"))
# if n==0:
#     print("number is 0")
# elif n>0:
#     print("number is positive")
# else:
#     print("number is negative")

# a=15
# b=15
# if a==b:
#     print("both are same")
# elif a>b:
#     print("A is greater")
# else:
#     print("B is greater")

# n=int(input("enter a number:"))

# if n%2==0:
#     print("number is even")
# else :
#     print("number is odd")


year=int(input("enter a year:"))
a=year%4
b=year%100
c=year%400
if a==0:
   
    if b==0:
       
       if c==0:
          print("leap year")
       else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")




