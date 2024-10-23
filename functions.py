# 1. Creating a Function
def my_function():
    # This function prints a greeting message
    print("Hello from a function")

# 2. Calling a Function
my_function()  # Output: Hello from a function

# 3. Arguments
def my_function(fname):
    # This function takes one argument and prints a greeting message
    print(fname + " Sharma")

my_function("Rahul")
my_function("Amit")
my_function("Vijay")

# 4. Number of Arguments
def my_function(fname, lname):
    # This function takes two arguments and prints a full name
    print(fname + " " + lname)

my_function("Rahul", "Sharma")  # Correct
# my_function("Rahul")  # Incorrect, will cause an error

# 5. Arbitrary Arguments, *args
def my_function(*kids):
    # This function takes an arbitrary number of arguments and prints the third one
    print("The youngest child is " + kids[2])

my_function("Rahul", "Amit", "Vijay")

# 6. Keyword Arguments
def my_function(child3, child2, child1):
    # This function takes keyword arguments and prints the third child
    print("The youngest child is " + child3)

my_function(child1="Rahul", child2="Amit", child3="Vijay")

# 7. Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
    # This function takes arbitrary keyword arguments and prints the last name
    print("His last name is " + kid["lname"])

my_function(fname="Rahul", lname="Sharma")

# 8. Default Parameter Value
def my_function(country="India"):
    # This function has a default parameter value
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# 9. Passing a List as an Argument
def my_function(food):
    # This function takes a list as an argument and prints each item
    for x in food:
        print(x)

fruits = ["apple", "banana", "mango"]
my_function(fruits)

# 10. Return Values
def my_function(x):
    # This function returns a value
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# 11. The pass Statement
def my_function():
    # This function does nothing (placeholder)
    pass

# 12. Positional-Only Arguments
def my_function(x, /):
    # This function takes a positional-only argument
    print(x)

my_function(3)
# my_function(x=3)  # Incorrect, will cause an error

# 13. Keyword-Only Arguments
def my_function(*, x):
    # This function takes a keyword-only argument
    print(x)

my_function(x=3)
# my_function(3)  # Incorrect, will cause an error

# 14. Combine Positional-Only and Keyword-Only
def my_function(pos1, /, pos_or_kwd, *, kwd1):
    # This function combines positional-only and keyword-only arguments
    print(pos1, pos_or_kwd, kwd1)

my_function(1, 2, kwd1=3)
# my_function(pos1=1, pos_or_kwd=2, kwd1=3)  # Incorrect, will cause an error
