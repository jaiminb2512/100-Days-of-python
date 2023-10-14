import time # Importing time library

def usingWhile():
  i = 0
  while i<50:
    i = i +1
    print(i) 

def usingFor():
  for i in range(50):
    print(i)

init = time.time() # Variable init store the current time
usingFor()
t1 = time.time() - init # Variable init store the time difference from 1970 to current time
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)


print(4)
time.sleep(3)
print("This is printed after 3 seconds")
 
t = time.localtime() 
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t) #In line of code variable stpre local time 

print(formatted_time) 