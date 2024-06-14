f=open("C:/Users/Python/Desktop/python_programs/assignments/file/file.txt","r")
# print(f.read())
# print(f.read(5))
# print(f.readlines())
f.close()

#with_open

with open("C:/Users/Python/Desktop/python_programs/assignments/file/file.txt","r+") as f:
    print(f.read())
     