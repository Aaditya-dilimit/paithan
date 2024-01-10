#reading file
'''
file = open("myfile",'r')
#print (type(file))
text = file.read()
print(text)
file.close()
'''

'''
with open("myfile",'r') as file:
    text = file.read()
    print(text)
'''

#write command 

'''
f = open('myfilew.txt', 'w')
f.write('Hello, world! write')
f.close()
'''

'''
with open('myfilew.txt', 'w') as f:
    f.write('Hello, world! write with open')
'''

#append command
'''
open('myfilew.txt', 'a')
f.write('Hello, world! append')
f.close()
'''