#day 14
x=int(input("Enter your marks : "))

if x<100:
    if (x > 33):
        print("You are passed")
        if (x > 90 and x < 100):
            print("your grade is A+")
        elif (x > 80 and x < 90):
            print("your grade is A")
        elif (x < 80 and x >= 60):
            print("your grade is b")
        elif (x < 60 and x >= 40):
            print("your grade is c")
        else:
            print("your grade is D")

    else:
        print("You are fail")
else:
    print("Invalid marks")
