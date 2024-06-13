# class add:
#     def add1(self,a,b):
#         x=a+b
#         return x
#     def add1(self,a,b,c):
#         x=a+b+c
#         return x
# bj=add()
# print(bj.add1(2,3,5))
# print(bj.add1(2,3))


# class dog:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f"{self.name}"" ""bark")
# class cat:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f"{self.name}"" " "mewo")
# dog1=dog("buddy")
# cat1=cat("kitty")
# dog1.speak()
# cat1.speak()

class animal:
    def __init__(self,name):
            self.name=name
    def speak(self):
            print("speak")

class dog(animal):
    def speak(self):
        print(f"the dog {self.name} bark")
class cat(animal):
    def speak(self):
        print(f"the cat {self.name} mewo")
dog1=dog("buddy")
cat1=cat("kitty")
dog1.speak()
cat1.speak()

    
    
