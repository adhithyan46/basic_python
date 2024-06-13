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

#dictionary comp
    
# list1=["red","green","apple","orange"]
# dict1={word:len(word) for word in list1}
# print(dict1) 

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
