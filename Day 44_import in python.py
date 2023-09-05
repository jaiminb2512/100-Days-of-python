# By importing modules "import math" from it's  name we have to use all the function by 
# name of modules and put dot(.) like this 
import math
a = math.sqrt(16)
print(a)

# Only one particlur function we can import from other modules
from math import sqrt
x = sqrt(9)
print(x)

# By use "from math import *" we importing all the function of that module
# But it is not recommeded 

# We can give lable to the particular operation 
from math import sqrt as s
y = s(25)
print(y)

# Getting all the function of any module we use dir function
import math
print(dir(math))

# Getting type of the function
print(math.nan,type(math.nan))

# By this we can import our python file as a module
from z import *
welcome()
print(jaimin)
