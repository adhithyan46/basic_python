# import zipfile
# with zipfile.ZipFile("C:/Users/Python/Desktop/python_programs/files/text.zip","w") as f:
#     f.write('C:/Users/Python/Desktop/python_programs/files/file1.txt')
#     f.write('C:/Users/Python/Desktop/python_programs/files/file2.txt')


# import zipfile
# with zipfile.ZipFile('C:/Users/Python/Desktop/python_programs/files/text.zip','r') as f:
#     f.extractall('extracted')


# import csv
# with open('C:/Users/Python/Desktop/python_programs/files/new_csv1.csv','w',newline='') as f:
#     w=csv.writer(f)
#     w.writerow(['name','place','age'])
#     w.writerow(['adhi',' kzm','  21'])
#     w.writerow(['ann','  kkm','  22'])


# import csv
# with open('C:/Users/Python/Desktop/python_programs/files/new_csv2.csv','w',newline='') as f:
#     w=csv.writer(f)
#     w.writerow(['name','place','age'])
#     w.writerow(['arun',' kkd','  21'])
#     w.writerow(['shibu','kkm','  22'])


# import zipfile
# with zipfile.ZipFile("C:/Users/Python/Desktop/python_programs/files/new_text.zip","w") as f:
#     f.write("C:/Users/Python/Desktop/python_programs/files/new_csv1.csv")
#     f.write("C:/Users/Python/Desktop/python_programs/files/new_csv2.csv")

import zipfile
with zipfile.ZipFile('C:/Users/Python/Desktop/python_programs/files/new_text.zip','r') as f:
    f.extractall('extracted')
    list1=f.namelist()
    print(list1)  