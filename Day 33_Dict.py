# in dictionary evry coma(,) show that the line is ending
# dictionary is ordered
# key = element of dictionary in first coloum
# In dictionary to store or access the the string you must use the Double inverted("") or single inverted('') comas
dict = {
    "Jaimin": "Human being",
    "Age" : "20",
    "Profession" : "Student"
}

#To generate empty dictionary
empty = {}
print(type(empty))

#To print whole dictionary
print(dict)

#if the key is not in dictionary this will show the error 
print(dict["Jaimin"])

#if the key we want is not in dictionary this will not show the error and print None
print(dict.get('Jaimin'))

#To access all the keys
print(dict.keys())

#To access all the values
print(dict.values())

# to access the value corespoding to keys
for key in dict.keys():
    print(dict[key])
    
for key in dict.keys():
    print(f"the values coresponding to {key} is {dict[key]}")
    
#To print kry and values in pair
print(dict.items())