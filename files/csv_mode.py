import csv
with open("C:/Users/Python/Desktop/python_programs/files/text.csv","w",newline='') as f:
    writer=csv.writer(f)
    writer.writerow(["name","  age","  place"])
    writer.writerow(["anna","  20","    kzm"])
    writer.writerow(["adhi","  20","    kazm"])

f= open("C:/Users/Python/Desktop/python_programs/files/text.csv","r")
reader=csv.reader(f)
for r in reader:
    print(r)