# Write a program to find missig numbers in an array of sequence
# Date : 25th April, 2024
# Author : Parmod

ls = [0,1,2,3,4,5,6,7,9] # 8 is missing in this list

def missing_number(ls):
    num=None
    for i in range(len(ls)-1):
        if ls[i]+1 == ls[i+1]:
            continue
        else:
            num = ls[i]+1
            break
    print(f"Missing number is : {num}")

missing_number(ls)
 