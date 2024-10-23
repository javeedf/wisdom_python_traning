# Basic input
user_input = input("Enter something: ")
print("You entered:", user_input)

# Integer input
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)

# Float input
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters")

# List input
data = input("Enter some numbers separated by spaces: ")
numbers = list(map(int, data.split()))
print("You entered:", numbers)

# Tuple input
data = input("Enter some numbers separated by spaces: ")
numbers = tuple(map(int, data.split()))
print("You entered:", numbers)

# Dictionary input
data = input("Enter key-value pairs separated by spaces (e.g., key1=value1 key2=value2): ")
pairs = dict(pair.split('=') for pair in data.split())
print("You entered:", pairs)
