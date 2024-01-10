keyy = input("key for dictonary")
val = eval(input("value(s) for the key"))

dictt = {keyy:val}
print (dictt)

import pickle 
file = open("dictt.dat",'wb')

pickle.dump(dictt , file)

file.close()

file = open("dictt.dat",'rb')
data = pickle.load(file)
print(data)