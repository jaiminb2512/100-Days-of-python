# Seek function is use to reding lines of files
with open ('Files/myfile.txt','r') as f:
    print(type(f))
# Move to the 10thbyte in file
    f.seek(10)

# Read the next 5 bytes 
    data = f.read(5)
    print(data)
        
# The  tell function returns the  current position within the file, in bytes.
    print(f.tell())
    
# Truncate is use to write no. of bytes in file
with open ('Files/myfile4.txt','w') as j:
    j.write("HELLO, JAIMIN HOW ARE YOU?")
    j.truncate(14)