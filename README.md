# phase3-wk1-code-challenge

# time_converter
The function time_converter is defined with three parameters: hour, minute, and period.

It starts by checking if the period is "am":

If the period is "am" and the hour is 12, it means it's 12 am (midnight), so the hour is reset to 0 (24-hour format representation of 12 am).

Next, it checks if the period is "pm":

If the period is "pm" and the hour is not 12, it means it's afternoon or evening. In this case, 12 needs to be added to the hour to convert it to the 24-hour format.

After handling the period conversions, the function constructs a formatted string using f-strings (f"{hour:02d}{minute:02d}"). This ensures that both the hour and minute values are represented with leading zeros if they are less than 10, ensuring a consistent two-digit format.

The function returns the constructed formatted string.

The code then calls the time_converter function with different input 


# positive_checker

The function exactly_two_positive is defined with three parameters: a, b, and c.

Inside the function, a list called positives is created using a list comprehension. This list contains three boolean values indicating whether each of the input numbers is positive (greater than 0).

The positive_count variable is assigned the count of True values in the positives list. This count represents the number of positive numbers among the three input values.

The function then returns True if the positive_count is equal to 2 (indicating exactly two positive numbers) and False otherwise.

The code provides several test cases by calling the exactly_two_positive function with different combinations of three numbers. The results of these tests are printed using the print function.



# consonant_checker

The function is defined and calculates the maximum value of consonant substrings within a given word. It follows these steps:

Initialize a string consonants containing consonant characters.

Create a dictionary values mapping each consonant to its alphabet position.

Define the function calculate_value to sum the values of characters in a substring.

Initialize max_value to track the highest value among consonant substrings.

Initialize an empty substring sub to temporarily store consecutive consonant characters.

Iterate through each character in the input word:

If it's a consonant, append it to the sub string.

If it's not a consonant, calculate the value of sub, update max_value if needed, and reset sub.

Calculate and compare the value of the last substring to update max_value.

Return the calculated max_value.
