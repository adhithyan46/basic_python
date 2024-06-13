# class Animal:#base class
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):#child class
#     def __init__(self, name, breed):
#         super().__init__(name)#inheriting base class
#         self.breed = breed
    
#     def speak(self):
#         return f"{self.name} the {self.breed} barks" #here methon from the base class (def speak()) will override

# dog = Dog("Buddy", "Golden Retriever")
# print(dog.speak())  

#adding a property 

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname,year):
#     super().__init__(fname, lname)
#     self.graduationyear = year #property added

# x = Student("Mike","Olsen",2019) #property passed as an arg
# print(x.graduationyear)
# x.printname()


# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Derived class
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    # def display_info(self):
    #     return f"{self.year} {self.make} {self.model} with {self.num_doors} doors"

# Create an instance of the derived class
my_car = Car("Toyota", "Camry", 2020, 4)

# Call the method from the derived class
print(my_car.display_info()) 
