# class person:
#     def __init__(self) :
#         self.name="adhi"
#         self.age=21
# p=person()
# print("name:{}".format(p.name))
# print("age:{}".format(p.age))

# class person:
#     def __init__(self,name,age) :
#         self.name=name
#         self.age=age
       
# p=person("adhi",21)
# print(p.name)
# print(p.age)


class person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def printname(self):
        print(f"{self.name} {self.age}")
p=person("adhi",21)
p.printname()

