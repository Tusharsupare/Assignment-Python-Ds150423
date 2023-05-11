# # create an empty dictionary
ascii_dict = {}

# Loop through the ASCII values of the letters from a-z
for values in range(97, 123):
    # Convert the ASCII value to a character using the chr() function
    # and store the pair in the dictionary
    ascii_dict[chr(values)] = values

# Print the resulting dictionary
print(ascii_dict)