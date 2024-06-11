
#public-no keywords,can be accessed from anywhere

# class person:
#     def __init__(self,name,age) :
#         self.name=name
#         self.age=age
#     def dsp(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
# p=person("adhi",20)
# p.dsp()


#private(__)

# class bank:
#     def __init__(self,accountNo,balance):
#         self.__accountNo=accountNo #private
#         self.__balance=balance #private
#     def __dis(self):
#         print("account number:",self.__accountNo)
#         print("Balance:",self.__balance)
# b=bank(123456,1000)
# b.__dis()

#protected(_)

class person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def _disp(self):
        print("name:",self._name)
        print("age:",self._age)
class std(person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)      
        self._roll_no=roll_no
    def disp(self):
        self._disp()
        print("roll no:",self._roll_no)  
s=std("adhi",21,39)
s.disp()

        
    
