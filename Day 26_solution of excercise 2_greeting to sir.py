import time
# Hour = int(time.strftime('%H'))
Hour = int(input("Enter Hour : "))

if (Hour > 0 and Hour <= 12):
    print("Good morning sir")
elif (Hour > 12 and Hour <=17):
    print("Good Afternoon sir")
elif (Hour > 17 and Hour <=24):
    print("Good Evening sir")    
else:
    print("Invalid input")