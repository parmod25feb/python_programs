# This program shows how to use a function defined in another file
# Date : 11th April, 2024
# Owner : Parmod Kumar

# import the method from the file addmethod.py
from addmethod import addfunc

# setting up a flag value
flag=True

# let's continue the program until the user wants
while flag:
    num1 =eval(input("Pls enter your number 1: "))
    num2 =eval(input("Pls enter your number 2: "))
    addfunc(num1,num2)

    num=eval(input("Enter 1 to continue or 0 to finish : "))
    if num == 1:
        flag=True
    else:
        flag=False
    