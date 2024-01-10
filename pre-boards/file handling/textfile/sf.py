#seek() and find()
'''
with open('file.txt','r') as file:
    file.seek(10) # Move the cursur to 10th bite in the file
    print(file.read(5)) # Read the next 5 bytes
    
    print (file.tell()) # Tell the position
'''

'''
with open('file-truncate.txt','w') as file:
    file.write("Hello, World!")
    file.truncate(5) #Remove all characters accept first five
'''