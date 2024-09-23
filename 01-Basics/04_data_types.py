#here i have used  "type(variable_name)" to check data type of that variable
# Integer is a whole number
age = 25
print("Age:", age, "| Type:", type(age))

# float is a decimal number
height = 5.9
print("Height:", height, "| Type:", type(height))  # Showing height with decimals

# String or char is text form
name = "Aavash"
print("Name:", name, "| Type:", type(name))  #can have a sentence or any type of text


# Boolean is true or false thats itt..!!!
is_student = True
print("Is Student:", is_student, "| Type:", type(is_student)) #will give result in True or False

# List is a collection of items which can be changed .
fruits = ["apple", "banana", "Mango"]
print("Fruits:", fruits, "| Type:", type(fruits))  # i added some fruits and check its type

# tuple is a collection of items that Can'T be changed
points = (1.0, 2.0)
print("Points:", points, "| Type:", type(points))  # Will showing points

# Dictionary is a collection of key value pairs with a unique key
person = {"name": "Aavash", "age": 18}
print("Person:", person, "| Type:", type(person))

# Set uses curly bracket but it doesnot allow duplicate value .
unique_numbers = {1, 2, 3, 4, 4, 5}
print("Unique Numbers:", unique_numbers, "| Type:", type(unique_numbers))  #will display numbers
