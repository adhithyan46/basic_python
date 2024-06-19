# try:
#     x=int(input("enter a number:"))
#     y=10/x
#     print(y)
# except ValueError:
#     print("enter a valid integer:")
# except ZeroDivisionError:
#     print("cannot divid by zero:")
# else:
#     print("successfully executed")
# finally:
#     print("execution completed")

# try:
#     with open ('new_file.txt','r') as f:
#         print(f.read())
# except FileNotFoundError:
#     print("enter a valid filename")


try:
    age=int(input("enter age:"))
    print("age is",age)
    if age<=0:
        raise ValueError('age must be greater that zero')
except ValueError:
    print("enter a valid age:")
else:
    print("your age is:",age)
finally:
    pass