# Day 2: 30 Days of python programming
## Exercises: Level 1

first_name = 'Friso' # Declare a first name variable and assign a value to it
last_name = 'Meeusen' # Declare a last name variable and assign a value to it
full_name = 'Friso Meeusen' # Declare a full name variable and assign a value to it
country = 'The Netherlands' # Declare a country variable and assign a value to it
city = 'Eindhoven' # Declare a city variable and assign a value to it
age = 24 # Declare an age variable and assign a value to it
year = 2001 # Declare a year variable and assign a value to it
is_married = False # Declare a variable is_married and assign a value to it
is_true = True # Declare a variable is_true and assign a value to it
is_light_on = False #Declare a variable is_light_on and assign a value to it
a,b,c = 10, 'baba', False #Declare multiple variable on one line

## Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print(f"first_name: {type(first_name)}")
print(f"last_name: {type(last_name)}")
print(f"full_name: {type(full_name)}")
print(f"country: {type(country)}")
print(f"city: {type(city)}")
print(f"year: {type(year)}")
print(f"is_married: {type(is_married)}")
print(f"is_true: {type(is_true)}")
print(f"is_light_on: {type(is_light_on)}")
print(f"a,b,c: {type(a), type(b), type(c)}")

# Using the len() built-in function, find the length of your first name
print(f"len(first_name): {len(first_name)}")

# Compare the length of your first name and your last name
print(f"lenght first_name vs last_name: {len(first_name), len(last_name)}")

# Declare 5 as num_one and 4 as num_two
num_one, num_two = 5,4
total = num_one + num_two  # Add num_one and num_two and assign the value to a variable total 
diff = num_one - num_two # Subtract num_two from num_one and assign the value to a variable diff 
product = num_one * num_two # Multiply num_two and num_one and assign the value to a variable product
division = num_one / num_two # Divide num_one by num_two and assign the value to a variable division
remainder = num_two % num_one # Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
exp = num_one**num_two # Calculate num_one to the power of num_two and assign the value to a variable exp
floor_division = num_one//num_two # Find floor division of num_one by num_two and assign the value to a variable floor_division

radius_of_circle = 30 #The radius of a circle is 30 meters
pi = 3.141592 # Define pi
area_of_circle = pi*(radius_of_circle**2) # Calculate the area of a circle and assign the value to a variable name of area_of_circle
circum_of_circle = 2*pi*radius_of_circle # Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

# Take radius as user input and calculate the area.
radius_by_user_input = input('what is the circle radius?')
print(f"circle area: {pi*(float(radius_by_user_input)**2)}") #Note that we have to convert the user-input from a string to float.

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("first_name?")
last_name = input("last_name?")
country = input("country?")
age = input("age?")

# Show that the output of the built-in input function is always a string. 
print(f"age: {type(age)}")

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')