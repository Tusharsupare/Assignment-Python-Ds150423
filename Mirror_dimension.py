# str = "Edyoda"
# reversed = '' 
# for e in str:
#     reversed = e + reversed 
# print(reversed)

words = input(str("Enter a word to send in Mirror Dimension :")) # inputs from the user
reversed = ''     # i created a empty string
for r in words:   # i used for loop to iterate over each character in the string
    reversed = r + reversed  #words given is concatenated to the beginning of the reversed variable. so its reversed the order 
print(reversed)    