# This program is to covert a binary number to decimal
# Date : 29th Apr, 2024
# Author : Parmod

num = eval(input("Please enter a binary number : ")) 

def binary_to_decimal(num):
    rem,res =0,0
    count=0
    while num !=0:
        rem= num%10
        res = res + (rem*pow(2,count))
        num=num//10
        count += 1
    return res


dec= binary_to_decimal(num)

print(f"\b For binary - {num} - decimanl is : {dec}")