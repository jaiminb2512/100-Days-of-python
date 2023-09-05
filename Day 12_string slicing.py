#day 12
#sring slicing
x = "harry"
print(x[0:3])
print(x[-4:-2])
 
#strings are immutable in python
#conver all character in to lower and upper case
x = "kdfdfHdjfojSJIHDkf"
print(x.lower())
print(x.upper())

#rstip is function to strip something but only back side of the strings
y="!!!!!jaimin!!!!"
print(y.rstrip("!"))
print(y.lstrip("!"))

#replace function is use to replace part of string in string
z = "jaimin !!!! jaimin"
print(z.replace("jaimin","coder"))