# This program will find and print the duplicate element in the list 
# Date : 15th April, 2024
# Author : Parmod Kumar

# Here is the list/array to find out duplicate items 
ls = [2,5,3,8,3,5,11,5]

# Function definition to find the duplicate items
def duplicate_element_in_list(ls):
    dic={}
    for item in ls:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    return dic

# Calling the function by passing the list as an argument and which return the dictionary
di = duplicate_element_in_list(ls)

print("\nHere are the duplicate items in the list :\n")

# Printing the duplicate elements
for key in di.keys():
    if di[key]>1:
        print(f"Item {key} occurres : {di[key]} times")