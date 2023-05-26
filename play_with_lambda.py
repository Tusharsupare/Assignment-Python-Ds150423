# Input from the user
user_input = float(input("Enter a number to add 25: "))

# Using Lambda
add_25 = lambda x: x + 25

# Assigniung Variable
output = add_25(user_input)

# Printing the output
print(f"Output of a given number is: {output}")