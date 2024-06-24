# f=open("text.txt","r")
# # print(f.read())
# print(f.readline())
# f.close()

with open("text.txt","r") as f:
    print(f.read())