# Define a function to convert 12-hour time to 24-hour time
def time_converter(hour, minute, period):
    # Check if the period is "am"
    if period == "am":
        # If it's 12 am, reset hour to 0
        if hour == 12:
            hour = 0
    # Check if the period is "pm"
    elif period == "pm":
        # If it's not 12 pm, add 12 to hour to convert to 24-hour format
        if hour != 12:
            hour += 12
    # Return the time in 24-hour format as a formatted string
    return f"{hour:02d}{minute:02d}"

# Call the function and print the results
print(time_converter(8, 30, "am")) 
print(time_converter(8, 30, "pm")) 

