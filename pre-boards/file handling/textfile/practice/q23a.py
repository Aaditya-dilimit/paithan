def count_you():
    file = open("Alpha.txt", "r")
    count = 0
    while True :
        line = file.readline()

        if not line:
            break
        
        if line.split()[0].lower() == 'you':
            count +=1
        
    print(count)


        
