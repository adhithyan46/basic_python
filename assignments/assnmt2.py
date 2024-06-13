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

#uppercase

# lines=[]
# print("enter 2 lines:")
# for _ in range(2):
#     line=input("enter line1:")
#     line=input("enter line2:") 
#     lines[0]=line

# print("capitalized")
# for line in lines:
#     print(lines.upper())

#dictionary merge

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


# #count of letters and digits

# sent=input("enter a sentence:")
# letters=0
# digits=0
# for i in sent:
#     if i.isalpha():
#         letters+=1
#     elif i.isdigit():
#         digits+=1
# print(f"number of letters:{letters}")
# print(f"number of digits:{digits}")


# #list comp

# list1=[1,2,3,4]
# list2=[i for i in list1 if i>2 ]  
# print(list2)


##dictionary comp
    
# list1=["red","green","apple","orange"]
# dict1={word:len(word) for word in list1}
# print(dict1) 


# #largest and smallest

# list1=[1,2,3,4,5]
# max=max(list1)
# min=min(list1)
# print(f"largest value:{max}")
# print(f"smallest value:{min}")

#removing even numbers

# list1=[1,2,3,4,5,6,7,8,9]
# list2=[i for i in list1 if i%2!=0]
# print(list2)
# print(len(list2))

#first and last 5 elements

# list1=[i**2 for i in range(1,31)]
# first_5=list1[:5]
# second_5=list1[-5:]
# print("first 5 elements:",first_5)
# print("second 5 elements:",second_5)


#inserting a given string at the begining

# list1=["red","green","blue"]
# str1="color:"
# list2=[str1+i for i in list1 ]
# print((list2))

#iterat throug 2 loop

# list1=["red","green","blue"]
# list2=["color1:","color2:","color3:"]
# # list3=list1.update(list1)
# for i1,i2 in (list1,list2):
#     print(i2,i1)

#adding key

dict1={
    "name":"adhi",
    "place":"kzm"
}
dict1["age"]=21
k=dict1.keys()
print(k)

#dict concat

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
# dic1.update(dic2)
# dic1.update(dic3)
# dic4.update(dic1)
# print(dic4)


#dict iteration


# dic1={
#     1:10,
#     2:20,
#     3:30
# }
# for key,value in dic1.item():
#     print(f"{key}:{value}")

# #sum of values in a dict

# dic1={
#      1:10,
#      2:20,
#      3:30
#  }
# dic_sum=sum(dic1.values())
# print(dic_sum)

#

# pets={
#     "dog":"kuttu",
#     "cat":"wikky",
#     "cow":"drake"
# }
# # print(pets)
# for pet,name in pets.items():
#     print(f"{name} is a {pet}")



#

# def mark(mark):
#     hig_marks={}
#     for s,m in mark.items():
#         if m >50:
#          hig_marks[s]=m
#     return hig_marks
# marks = {
#         "English": 40,
#              "Maths": 60, 
#              "Hindi": 30,
#              "Chemistry": 46,
#              "Physics": 70
#              }
# highest=mark(marks)
# print("subject having marks more than 50",highest)                                                                                  
