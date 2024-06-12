from abc import(ABC,abstractmethod)
from math import pi
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def peri (self):
        pass
class rect(shape):
    def __init__(self,length,height):
        self.length=length
        self.height=height
    def area(self):
        print("area of rectangle:",self.length*self.height)
    def peri(self):
        print("perimeter of rectangle:",2*(self.length+self.height))
class cir(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("area of circle:",pi*self.radius**2)
    def peri(self):
        print("perimeter of circle:",2*pi*self.radius)
rectangle=rect(10,5)
rectangle.area()
rectangle.peri()
circle=cir(5)
circle.area()
circle.peri()

#

from abc import(ABC,abstractmethod)
class animal(ABC):
    @abstractmethod
    def speak(self):
     pass
class dog(animal):
    def __init__(self,name):
      self.name=name
    def speak(self):
       print(f"The dog {self.name} barks")
class cat(animal):
    def __init__(self,name):
       self.name=name
    def speak(self):
       print(f"The cat {self.name} meows")
class bird(animal):
    def __init__(self,name):
       self.name=name
    def speak(self):
       print(f"The bird {self.name} chirp")
d=dog("wikky")
d.speak()
c=cat("tom")
c.speak()
b=bird("lily")
b.speak()
    







