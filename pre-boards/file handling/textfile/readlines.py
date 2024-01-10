'''
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        
        break
    print(line)
'''

'''
f = open('myfile.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1}")
  print(f"Marks of student {i} in English is: {m2}")
  print(f"Marks of student {i} in SST is: {m3}")

  print(line)
'''

'''
f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
'''

'''
f = open('myfile2.txt', 'w')
line1 = "hello how are you"
line2 = "I'm fine what about you"
line3 = "me too"
lines = f'{line1}\n{line2}\n{line3}'
f.write(lines)
f.close()
'''
'''
f = open('myfile2.txt', 'w')
line1 = "hello how are you"
line2 = "I'm fine what about you"
line3 = "me too"
lines = ['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()
'''
