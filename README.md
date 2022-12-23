# Python Variables & Methods 
## Basic Variables & Methods written in Python Languages
  
Now that we have a simple understanding of how we can use Python. Let's see how we can use Python to make 
variables & methods!
And these simple commands will give us aid & support in doing that.
 

# Creating & Calling Variables
*By creating & setting variables, we can call them later and use them as many times as we need too!*
```
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
```

# Creating a Function
*Functions allows us to put all of our variables into 1 section and then call that function later on as we need it!  
```
def who_am_i():
	name = "Crypto H4ck3r" 
	age = 32
	print("My name is " + name + " and I am " + str(age) + " years old!")

who_am_i()
```

# Functions to use Math;
*In this example, we will see how we can use a Function to call a Variable in order to Add 2 numbers together!
```
def add(x, y):
	print(x + y)
print("If we add 7 + 7, we get; ")
add(7,7)
```
