def square_root(number):
    return number ** 2

# Given Sample List    
given_list = [4, 5, 2, 9]

# using map() to get squared numbers
squared_list = list(map(square_root,given_list))
print("Original List:", given_list)
print("Squared List:", squared_list)
