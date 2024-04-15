# This program will find and print the duplicate element in the list 
# Date : 15th April, 2024
# Author : Parmod Kumar

# Here is the string 
st1 = "domraP ramuK amrahS Rashmi"

# Function to reverse the words of the string 
def reverse_of_words(st):
    ls=st.split(' ')
    result_str=" "
    for word in ls:
        for ch in range(len(word)-1,-1,-1):
            result_str +=(word[ch])
        result_str +=" "
    return result_str

# Calling the function by passing the string as an argument 
s= reverse_of_words(st1)

# Printing the original and the reverse strings
print(f"\nYour original string : {st1}")
print(f"\nResult string with the reverse of the words : {s}\n\n")
