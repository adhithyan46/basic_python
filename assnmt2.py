#1.transpose

# mat=[
#     [1,2],
#      [3,4],
#      [5,6]
#      ]

# trans= [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0])) ]
# print("original matrix:")
# for i in mat:
#     print(i)
# print("transpose:")
# for i in trans :
#     print(i)

#2.uppercase

lines=[]
print("enter 2 lines:")
for _ in range(2):
    line=input("enter line1:")
    line=input("enter line2:")
    lines[0]=line

print("capitalized")
for line in lines:
    print(lines.upper())

#3.dictionary merge

# dict1={}
# dict2={}
# print("enter key-value pair")
# for _  in range(3):
#     key=input("enter key:")
#     value=input("enter value:")
#     dict1[key]=value
# print("1st dictionary")
# print(dict1)

# print("enter key-value pair")
# for _ in range(3):
#     key=input("enter key:")
#     value=input("enter value:")
#     dict2[key]=value
# print("2st dictionary")
# print(dict2)
# dict3=dict1|dict2
# print("merged dictionary")
# print(dict3)

#4.list methods

list1=[1,2,3,4]
list2=[5,6,7,8]
list1.append(list2)
print("list after appending")
print(list1)
list1.pop()
print("list after pop")
print(list1)
list1.remove(3)
print("list after removing")
print(list1)
i=list1.index(4)
print("index of 6")
print(i)
c=list1.count(2)
print("count of 2")
print(c)
list1.clear()
print("list after clear")
print(list1)


#5.dictionary methods

dict1={
    "name":"a",
    "age":"b"
}
dict2={
    "place":"c",
    "city":"d"
}
v=dict1.values()
print("values of dictionary")
print(v)
k=dict1.keys()
print("keys of dictionary")
print(k)
i=dict1.get("name")
print("name is:")
print(i)
dict1.update({"mob":"n"})
print("updated dictionary:")
print(dict1)
dict3=dict1.copy()
print("copy")
print(dict3)
dict1.clear()
print("dictionar cleared")
print(dict1)

#6.sum element in a list

list1=[1,2,3,4,5]
sum=0
for i in list1:
    sum+=i
print(sum)

#7.list comp

list1=[1,2,3,4]
list2=[i for i in list1 if i>2 ]  
print(list2)

#8.largest and smallest

list1=[1,2,3,4,5]
max=max(list1)
min=min(list1)
print(f"largest value:{max}")
print(f"smallest value:{min}")

#9
list1=[1,2,3,4,5,6,7,8,9]
list2=[i for i in list1 if i%2!=0]
print(list2)
print(len(list2))

#10
list1=[i**2 for i in range(1,31)]
first_5=list1[:5]
second_5=list1[-5:]
print("first 5 elements:",first_5)
print("second 5 elements:",second_5)

#11

list1=["red","green","blue"]
str1="color:"
list2=[str1+i for i in list1 ]
print((list2))

#12
dict1={
    "name":"adhi",
    "place":"kzm"
}
dict1["age"]=21
k=dict1.keys()
print(k)

#13

list1=["red","green","apple","orange"]
dict1={word:len(word) for word in list1}
print(dict1)  

#14 dictionary concatination

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
dic1.update(dic2)
dic1.update(dic3)
dic4.update(dic1)
print(dic4)

#15 iteration over dictionary

dic1={
    1:10,
    2:20,
    3:30
}
for key,value in dic1.item():
    print(f"{key}:{value}")

#16sum of values in a dict

dic1={
     1:10,
     2:20,
     3:30
 }
dic_sum=sum(dic1.values())
print(dic_sum)

#17 dict

pets={
    "dog":"kuttu",
    "cat":"wikky",
    "cow":"drake"
}
# print(pets)
for pet,name in pets.items():
    print(f"{name} is a {pet}")

#18

def mark(mark):
    hig_marks={}
    for s,m in mark.items():
        if m >50:
         hig_marks[s]=m
    return hig_marks
marks = {
        "English": 40,
             "Maths": 60, 
             "Hindi": 30,
             "Chemistry": 46,
             "Physics": 70
             }
highest=mark(marks)
print("subject having marks more than 50",highest)

