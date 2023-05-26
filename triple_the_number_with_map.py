# Using Function
def triple_no(numbers):
    return list(map(lambda x: x * 3, numbers)) # assigning map function

sample_lst = [1, 2, 3, 4, 5, 6, 7]    
result = triple_no(sample_lst)  # Assigning variable
print(f"The value with triple number ---> {result}") 
