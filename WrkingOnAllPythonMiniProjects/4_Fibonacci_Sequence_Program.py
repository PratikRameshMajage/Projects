def fibonacci_sequence(n):
    # Set the first two terms of the sequence
    a, b = 0, 1
    
    # Iterate from 0 to n
    for i in range(n):
        # Print the current term
        print(a, end=' ')
        # Calculate the next term by adding the previous two terms
        a, b = b, a + b

# Take input from the user
n = int(input("Enter the number of terms: "))

# Call the function to generate the sequence
fibonacci_sequence(n)
