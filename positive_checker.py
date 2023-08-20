# Define a function to check if exactly two out of three integers are positive
def exactly_two_positive(a, b, c):
    # Create a list of booleans indicating whether each number is positive
    positives = [x > 0 for x in [a, b, c]]
    
    # Count the number of positive numbers in the list
    positive_count = positives.count(True)
    
    # Return True if exactly two numbers are positive, otherwise return False
    return positive_count == 2

# Call the function and print the results
print(exactly_two_positive(2, 4, -3))  
print(exactly_two_positive(-4, 6, 8))  
print(exactly_two_positive(4, -6, 9))  
print(exactly_two_positive(-4, 6, 0))  
print(exactly_two_positive(4, 6, 10))  
print(exactly_two_positive(-14, -3, -4))  

