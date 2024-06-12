import math
class triangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @staticmethod
    def hypo(a,b):
        return"hypotenuse=",math.sqrt(a**2+b**2)
tri=triangle(6,2)
print(tri.hypo(6,2))