my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(len(my_list)):  # 0 to len(my_list)-1
    min_index = i        # variable is used to keep track of the index of tuple with the smallest second integer value.
    for j in range(i + 1, len(my_list)):   # nested for loop that iterates over each index j in the range i+1 to len(my_list)-1
        if my_list[j][-1] < my_list[min_index][-1]:  # if is use to check the  2nd value of tuple  j < 2nd integer value of min index 
            min_index = j
    my_list[i], my_list[min_index] = my_list[min_index], my_list[i] # outer loop then proceeds to the next index & repeats steps 3-6 until all elements have been sorted

print(my_list)

