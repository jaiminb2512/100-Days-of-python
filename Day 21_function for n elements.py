# Making function to find avareage of n numbers
def avgofnum(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        print("Avg is: ", sum / len(numbers))


avgofnum(52, 644, 8)


def name(**name):
    print("hello", name['fname'], name["mname"], name["lname"])


name(fname="Jaimin", mname="Bharatbhai", lname="Prajapati")
