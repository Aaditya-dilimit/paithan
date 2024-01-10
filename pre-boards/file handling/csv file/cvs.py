import csv

'''writing rows
data = [
    ("Surendra", 12345, "charsi", "pandru"),
    ("Nem sing", 25896, "ganjedi", "Lakra")
]
with open("new.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(data)
'''

'''
# writing row
data = ["Vishal", 74125, "randi ka baccha", "nepali"]

with open("new.csv", "a" , newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data)
'''
    
'''
#accessing line by line
with open ("new.csv","r") as file :
    reader = csv.reader(file)
    
    for data in reader :
        print(data)
'''

'''
#accessing all datas at once
file = open("new.csv","r")
reader = csv.reader(file))
print(list(reader))
file.close()
'''







