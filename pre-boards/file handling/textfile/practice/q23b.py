def vovelcount():
    file = open("Poem.txt",'r')
    count = 0
    vovels = ('a','e','i','o','u')
    data = file.read()
    for i in data:
        if i.lower() in vovels:
            count +=1
            return count
vovelcount()
print 