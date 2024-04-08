# This is the python program to count characters occurrence in the string
# Date: 08 April, 2024
# Author : Parmod Kumar

# Asking the user to provide the string
st = input("Please enter your string : ")
# Function definition
def charcountfunction(str):
    dic = {}
    for ch in str:
        if ch in dic:
            dic[ch]=dic[ch]+1
        else:
            dic[ch]=1
    return dic
# Calling the function
d = charcountfunction(st)

# Printing the occurrences
for key in d.keys():
    print(f"{key} occurrs -  {d[key]} times")
