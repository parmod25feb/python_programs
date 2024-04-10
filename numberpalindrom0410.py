# This program will show if a number is palindrom or not 
# Date : 10th April, 2024
# Owner : Parmod Kumar

# User will enter the number
num = eval(input("Please enter your number : "))

# This is function definition
def is_palindrome(num):
    num1=num
    rev=rem=0
    while num1 !=0:
        rem = num1%10
        rev = rev*10+rem
        num1=num1//10
    if num == rev:
        print(f"Palindrom - {num} is equal to it's reverse {rev}\n")
    else:
        print(f"Sorry, number is not palindrom as {num} is not equal to {rev}\n")

# Calling the function to check if nubmer is reverse or not 
is_palindrome(num)