#!/bin/python3

# This Python script will demonstrate how we can create variables as well as print them and call out floating variables in our commands.

# This script will be based upon Personal Information. Please adjust according to your personal information.

# Create a basic function that will allow us to create a line spacer;
def nl():
	print('\n')

# Call a variable titled "movie";
movie = "The Matrix"
# Now call another variable titled "name";
name = "Crypto H4ck3r"
# We are going to call another variable for our "age";
age = 32
# And finally, we will call another one for our "gpa";
gpa = 3.8
# Now we will call these individually and have them displayed on our terminal screens;
print("Greatest Movie is " + movie)
print("My name is " + name)
print("I am " + str(age) + " years old!")
print("My College GPA was " + str(gpa))
age += 1
print("In March, I will be " + str(age))

# Start Python Function Methods
# Create a new basic function;
print("This is an example of a function:")
nl()
# Start a Define Function;
def who_am_i():
	name = "Crypto H4ck3r" 
	age = 32
	print("My name is " + name + " and I am " + str(age) + " years old!")

who_am_i()
nl()
# New Function to include Parameters;
def add_one_hundred(num):
	print(num + 100)

print("If we use the number 1, and add 100 to it, we get;")
add_one_hundred(1)
nl()
# Now we will work with Multiple Parameters in which will allow us to use multiple numbers for math equations. We can do it like so;

# Create a new Function for Adding 2 numbers;
def add(x, y):
	print(x + y)
print("If we add 7 + 7, we get; ")
add(7,7)
nl()
# Create a new Function for Multiplication;
def multiply(x,y):
	return x * y
print("The answer to 7 x 7 is ") 
print(multiply(7,7))
nl()
# Create a new Function for getting the Square Root of a Number;
def square_root(x):
	print(x ** .5)

print("Square root of 64 is ")
square_root(64)
nl()
# Getting Started with Boolean Statements;

# A boolean is basically asking/saying something is either True or False!

# Check out the example below;
print("Boolean Expressions:")
bool1 = True
bool2 = 3*9 == 9
bool3 = False 
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))
nl()
def beer(age,money):
	if(age >= 21) and (money >= 5):
		return "You're getting a Pint of Guinness!"
	elif (age >= 21) and (money < 5):
		return "You need more Pounds mate!"
	elif (age < 21) and (money >= 5):
		return "Nice try kid, get out of my Pub!"
	else:
		return "Kid, turn 21, and come back with at least 5 pounds next time!"

print(beer(21,8))
print(beer(25,1))
print(beer(19,50))
nl()

# Create a list that will display our favorite movies;
movies = ["Hackers", "Sneakers", "Good Will Hunting", "Star Wars"]

# Now we will print off our movie list in multiple ways;
print(movies[0]) # Prints off the first movie title. Lists start with 0 (Zero) and go up from there!
print(movies[1]) # Prints off the second movie title.
print(movies[1:4]) # Prints off the second movie title all the way to the "third" or last movie title.
print(movies[:2]) # Prints off the first 2 movies and will stop pulling data upon the 3rd slot.
print("The total number of Movie Titles in the list is;")
print(len(movies))

# Now we can Append, or add, a new movie to the end of the list by the following;
movies.append("Blackhat")
print(movies) # Prints all movie titles and adds the "Blackhat" movie at the end;

# If we want to delete the last entry of the list, we can use POP like so;
movies.pop() # Removes the last entry of our list.
print(movies)
# If we wanted to remove the very first entry in our list, we can add a 0 in the brackets like so;
movies.pop(0)
print(movies)

