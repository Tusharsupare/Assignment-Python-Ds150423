# getting the user input for the fibonacci series
user = int(input("Enter the number to Start : \n Fibonacci sequence: "))

# the first two terms of the Fibonacci series
fib_a, fib_b = 0, 1

# the first two terms of the Fibonacci Series ae printed
print(fib_a)
print(fib_b)

# loop i used to calculate remaining  term of the series 
for i in range(user - 2): # user - 2 is used in loop since the first two term has already taken

  # inside the loop, the next term in the series is calculated by adding the previous two terms
    fib_c = fib_a + fib_b

  # The values of fib_a and fib_b are updated for the next iteration of the loop.
    fib_a = fib_b
    fib_b = fib_c
    
    # Printing the term in sequence
    print(fib_c)