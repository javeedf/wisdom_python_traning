# Arithmetic Operators
a = 10
b = 3

# Addition: Adds two operands
add = a + b  # 13

# Subtraction: Subtracts the second operand from the first
sub = a - b  # 7

# Multiplication: Multiplies two operands
mul = a * b  # 30

# Division: Divides the first operand by the second
div = a / b  # 3.333...

# Modulus: Returns the remainder of the division
mod = a % b  # 1

# Exponentiation: Raises the first operand to the power of the second
exp = a ** b  # 1000

# Floor Division: Divides and returns the largest integer less than or equal to the result
floor_div = a // b  # 3

# Assignment Operators
x = 5

# Add and Assign: Adds and assigns the result
x += 3  # x is now 8

# Subtract and Assign: Subtracts and assigns the result
x -= 3  # x is now 5

# Multiply and Assign: Multiplies and assigns the result
x *= 3  # x is now 15

# Divide and Assign: Divides and assigns the result
x /= 3  # x is now 5.0

# Modulus and Assign: Takes modulus and assigns the result
x %= 3  # x is now 2

# Exponentiate and Assign: Raises to the power and assigns the result
x **= 3  # x is now 8

# Floor Divide and Assign: Floor divides and assigns the result
x //= 3  # x is now 2

# Comparison Operators
y = 10
z = 20

# Equal: Checks if two values are equal
equal = (y == z)  # False

# Not Equal: Checks if two values are not equal
not_equal = (y != z)  # True

# Greater Than: Checks if the left operand is greater than the right
greater_than = (y > z)  # False

# Less Than: Checks if the left operand is less than the right
less_than = (y < z)  # True

# Greater Than or Equal To: Checks if the left operand is greater than or equal to the right
greater_equal = (y >= z)  # False

# Less Than or Equal To: Checks if the left operand is less than or equal to the right
less_equal = (y <= z)  # True

# Logical Operators
a = True
b = False

# AND: Returns True if both statements are true
logical_and = a and b  # False

# OR: Returns True if one of the statements is true
logical_or = a or b  # True

# NOT: Reverses the result, returns False if the result is true
logical_not = not a  # False

# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# Is: Returns True if both variables are the same object
is_operator = (a is b)  # True

# Is Not: Returns True if both variables are not the same object
is_not_operator = (a is not c)  # True

# Membership Operators
a = [1, 2, 3, 4, 5]

# In: Returns True if a sequence with the specified value is present in the object
in_operator = (3 in a)  # True

# Not In: Returns True if a sequence with the specified value is not present in the object
not_in_operator = (6 not in a)  # True

# Bitwise Operators
a = 10  # 1010 in binary
b = 4   # 0100 in binary

# AND: Sets each bit to 1 if both bits are 1
bitwise_and = a & b  # 0 (0000 in binary)

# OR: Sets each bit to 1 if one of two bits is 1
bitwise_or = a | b  # 14 (1110 in binary)

# XOR: Sets each bit to 1 if only one of two bits is 1
bitwise_xor = a ^ b  # 14 (1110 in binary)

# NOT: Inverts all the bits
bitwise_not = ~a  # -11 (inverts all bits)

# Left Shift: Shift left by pushing zeros in from the right and let the leftmost bits fall off
left_shift = a << 2  # 40 (101000 in binary)

# Right Shift: Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
right_shift = a >> 2  # 2 (10 in binary)
