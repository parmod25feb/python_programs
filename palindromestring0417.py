# Write a program to check if the string is palindrome or not   
# Date : 17th April, 2024
# Author : Parmod Kumar

# Ask user to enter the value
st = input("Pls enter your string : ")
# let's convert the string in the lower case
s=st.lower()

# Function to get the reverse of the string
def reverseofstring(s):
    st1=""
    for i in range(len(s)-1,-1,-1):
        st1 +=s[i]
    return st1

# Calling function and store the string reverse in rev variable
rev= reverseofstring(s)

# Check if the reverse of the string is equal to the string or not
if s == rev:
    print(f"Congratulations! {s} is palindrome of - {rev}")
else:
    print(f"Sorry! {s} is not a palindrome of - {rev}")