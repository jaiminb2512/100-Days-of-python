# To read line of file
f = open('Files/Myfile.txt','r')
while True :
    line = f.readline()
    print(line)
    if not line:
        break
    
f = open('Files/Myfile3.txt','r')
i= 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in Math is: {m1}")
    print(f"Marks of student {i} in English is: {m2}")
    print(f"Marks of student {i} in Science is: {m3}")
    
# writelines statement
f = open('Files/myfile4.txt','w')
lines = ['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()    