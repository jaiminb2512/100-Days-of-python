info = "hey my name is {} and i am fron {}"
name = input("Enter your name : ")
country = input("Enter your country : ")

print(info.format(name,country))

print(f"hey my name is {name} and i am from {country}")

#to show {} in print use double curly braces
print(f"hey my name is {{name}} and i am from {{country}}")

price = 5465.654684845
txt=f"For only {price:.2f} dollars!"
print(txt)

#we can use format function like this

txt="For only {value:.2f} dollars!"
print(txt.format(value = 545.546546464))
