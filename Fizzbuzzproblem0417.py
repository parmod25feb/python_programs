# This program is for FiZZbuzz problem"  
# Date : 17th April, 2024
# Author : Parmod Kumar

# Ask user to enter the value
mx= eval(input("Pls enter the max value : "))
# Fizzbuzz logic
def fizzbuzz(mx):
    for num in range(mx):
        if num%5==0 and num %3==0:
            print(f"Fizzbuzz...{num}")
        elif num%5 == 0:
            print(f"Buzz - {num}")
        elif num%3==0:
            print(f"Fizz - {num}")

# Calling the function
fizzbuzz(mx)