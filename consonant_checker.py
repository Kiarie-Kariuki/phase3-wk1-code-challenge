def check(word):
    # Define a string containing consonant characters
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    # Create a dictionary that maps each consonant to its value
    values = {c: ord(c) - ord('a') + 1 for c in consonants}
    
    # Define a function to calculate the value of a substring
    def calculate_value(sub):
        return sum(values[c] for c in sub)
    
    # Initialize the maximum value variable
    max_value = 0
    
    # Initialize an empty substring to store consonant characters
    sub = ""
    
    # Loop through each character in the input word
    for char in word:
        if char in consonants:
            # If the character is a consonant, add it to the current substring
            sub += char
        else:
            # If the character is not a consonant, calculate the value of the current substring
            value = calculate_value(sub)
            # Update the maximum value if the current value is greater
            if value > max_value:
                max_value = value
            # Reset the current substring
            sub = ""
    
    # Calculate the value of the last remaining substring if it ends with a consonant
    value = calculate_value(sub)
    # Update the maximum value if the last substring's value is greater
    if value > max_value:
        max_value = value
    
    # Return the maximum value of consonant substrings
    return max_value

#Call the function and print the output.
print(check("zodiacs"))
print(check("strength"))