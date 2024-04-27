# This program is to covert a decimal to binary
# Date : 27st Apr, 2024
# Author : Parmod



def decimal_to_binary(num):
    rem=0
    st=""
    while num !=0:
        rem=num%2
        st = str(rem) + st
        num=num//2
    n=''.join(st)
    return n

flag = True
while flag:
    num = int(input("\nPlease enter your decimal number : "))
    #Calling the decimal to binary conversion
    bi = decimal_to_binary(num)
    print(f"\nBinary conversion of {num} is : {bi}")

    ch = eval(input(f"\nPress 1 to continue and 0 to exit : "))
    if ch == 1:
        flag = True
    else :
        flag = False

