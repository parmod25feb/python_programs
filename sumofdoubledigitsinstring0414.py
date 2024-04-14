# This program will calculate the sum of double digits in the string like - a12b13c8 = 33
# Date : 14th April, 2024
# Author : Parmod Kumar

def sum_of_digits(string):
    current_number = ""
    total_sum = 0
    
    for char in string:
        # print(char)
        if char.isdigit():
            # If the character is a digit, add it to the current number
            current_number += char
        else:
            # If the character is not a digit, add the current number to the total sum
            if current_number:
                total_sum += int(current_number)
                current_number = ""
                print(total_sum)
    
    # Add the last number if there is any
    if current_number:
        total_sum += int(current_number)
    
    return total_sum

# Example usage:
string = "a12b13c8"
result = sum_of_digits(string)
print("Sum of digits:", result)
