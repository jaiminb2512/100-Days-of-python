# Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.
# In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called
# Cache will clear after code is excuted once. That means when you run the program again the computation is done by computer again
# The cache is also taking the 
# This is useful when the values are less and function call many times

from functools import lru_cache
import time

@lru_cache(maxsize=None) 
def fx(n):
  time.sleep(5)
  return 2*n    

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

#This block of code is alreday computed so that all this command are excuted without coputation 
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")


print(fx(61))
print("done for 61")

