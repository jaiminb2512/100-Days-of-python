#day 16
x = int(input("Enter the value of x : "))

match x:
    case 0:
        print("Entered value of",x,"is zero")

    case 1:
        print("Entered value of", x, "is one")

    case _ if x!=90:
        print("Entered value of", x, "is not sixty")

    case _ if x != 80:
        print("Entered value of", x, "is not eighty")


    case _ :
        print(x)