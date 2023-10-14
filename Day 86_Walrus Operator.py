"""This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements."""

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

Mood = True
print(Mood) # Printing Mood variable 
print(Mood := False) # Making Mood variable false
print(Mood)  # After Making Mood is flase it will false to make it true we have to re-define it7


# We making a list by user input

# Using while loop
# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)

# Using Walrus Operator
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
# This code is same as above