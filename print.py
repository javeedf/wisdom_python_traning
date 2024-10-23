# Basic print() function
print("Hello, World!")

# Printing multiple items
print("Hello", "World", 123)

# Formatted strings (f-strings)
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# String concatenation
name = "Alice"
print("Hello, " + name + "!")

# Using str.format() method
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# Old-style string formatting
name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))

# Printing with separators
print("Hello", "World", sep=", ")

# Printing with end character
print("Hello", end=" ")
print("World!")

# Printing to a file
with open("output.txt", "w") as file:
    print("Hello, World!", file=file)

# Printing with flush
import time
for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(1)
