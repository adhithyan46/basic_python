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

#3.list methods

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


