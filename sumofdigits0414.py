# This program will calculate the sum of digits in the string like - a1b2c3 = 6
# Date : 14th April, 2024
# Author : Parmod Kumar

str = 'a4b2c6'

def sumofdigits(st):
    num=0
    for ch in st:
        if ch.isnumeric():
            num=num + int(ch)
    print(f"\nSum of digits are : {num}\n")


sumofdigits(str)