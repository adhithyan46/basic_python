# def func():#defining a generator function
#     yield 1
#     yield 2
#     yield 3
# x=func()
# for i in x:
#     print(i)



# def fun():
#     for i in range(20):
#         if (i%2==0):
#             yield i
# x=fun()
# for i in x:
#     print(i)

#iterator

# tup=("apple","orange","kiwi")
# tup="adhithyan"
# ite=iter(tup)
# print(next(ite))
# print(next(ite))
# print(next(ite))
# print(next(ite))


#iterator in class

# class num:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# mycls=num()
# myit=iter(mycls)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))



class num:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
       
        if self.a<=10:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration

mycls=num()
myit=iter(mycls)
for x in mycls:
    print(x)


class sqr:
    def __iter__(self):
        self.l=0
        return self
    def __next__(self):
       
        if self.l<=10:
            # x=self.l
            self.l+=1
            a=self.l**2
         
            return a
        else:
            raise StopIteration
            
#

mycls=sqr()
myit=iter(mycls)
for a in mycls:
    print(f"area ={a}")

  
