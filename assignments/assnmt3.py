##1

# class string:
#     def __init__(self):
#         self.input_str=""
#     def str1(self):
#      self.input_str=input("enter a string:")
       
#     def cap(self):
#         print(self.input_str.upper()) 
        
# s=string()
# s.str1()
# s.cap()

##2

# class para:
   
#   parmeter="hello world !"
#   def __init__(self):
#       self.msg="hello world !"
#   def parameters(self):
#      print(f"class parametr:{para.parmeter}")
#      print(f"instance parametre:{self.msg}")
         
    
# c=para()
# c.parameters()

##3 area of a circle

# class circle:
    
#     def __init__(self):
#         self.radius=""
#     def rad(self):
#         self.radius=int(input("enter the radius:"))
#     def area(self):
#         from math import pi
#         print("Area of the circle=",pi*self.radius**2)
# c=circle()
# c.rad()
# c.area()

##bank account

class bank_ant:
    def __init__(self):
        self.dpst=""
        self.wd=""
    def deposit(self):
        self.dpst=int(input("Enter the amount you deposited:"))
    def withdraw(self):
        self.wd=int(input("Enter the withdrawed amount:"))
    def balance(self):
        print("The balance amount in your bank account is",self.dpst - self.wd)
b=bank_ant()
b.deposit()
b.withdraw()
b.balance()

##area of the square

class shape:
    def __init__(self):
       pass
    def area(self):
        self.area=0
class square(shape):
    def __init__(self, length):
        self.length=length
        
    def area(self):
        print("area of the square=",self.length**2)
s=square(2)
s.area()
