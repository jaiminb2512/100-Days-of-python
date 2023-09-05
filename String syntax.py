x = "hello"
print(x)

#Print individual chcaracter
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

"""if the number in square bracket is higher than length of string it shows error
   print(x[5])   """

"""if you want to print like this
    hello, how are you ??
    hey, i am fine.
    what's about you.
    i am good."""
text = """hello, how are you ??
    hey, i am fine.
    what's about you.
    i am good."""

print(text)
#you can use single triple coats

#you can print all charcter using loop

for charcter in text:
    print(charcter)

#get how many character in your string
print(len(text))

A = "Prajapati jaimin bharatbhai"
if "jai" in "jaimin":
    print("YES")

else:
    print("NO")