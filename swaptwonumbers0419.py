# The program is to remove duplicate elements from the array
# Date : 19th April, 2024
# Author : Parmod Kumar

num1 = 5
num2 = 8
print(f"Numbers before swap : Num1 = {num1} & Num2 = {num2}")
def swap_numbers(num1,num2):
    num1,num2=num2,num1
    print(f"Numbers after swap : Num1 = {num1} & Num2 = {num2}")

swap_numbers(num1,num2)

def swap_numbers_with_temp(num1,num2):
    temp = num1
    num1=num2
    num2=temp
    print(f"Numbers after swap with help of a temp : Num1 = {num1} & Num2 = {num2}")
swap_numbers_with_temp(num1,num2)