# By given statement we can get access the files
# r for read
# w for write
# a  forappened
# If user doesn't define the mode then it assumed file open for read mode
f = open('Files/Myfile.txt','r')
text = f.read()
print(text)
f.close()

# If user doesn't define the mode then it assumed file open for read mode
f = open('Files/Myfile.txt')
text = f.read()
print(text)
f.close()

# When user try to write file which doesn't exist then python make that file 
f = open('Files/Myfile2.txt','w')

# For writing in file
# When we open file in write mode and then we write in that it will erase the peiveous data and write new data which we add in code 
f = open('Files/Myfile2.txt','w')
f.write('hello,jaimin')


# When we open file in append mode and then we write in that it will  not erase the peiveous data and write new data which we add in code 
f = open('Files/Myfile2.txt','a')
f.write('hello,jaimin')

# To close file
f.close()


# Second method to io file
# By this method we doesn't need to close file
with open('Files/Myfile2.txt','a') as f:
    f.write('How are you?')